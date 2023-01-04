# Django
from django.contrib.auth import get_user_model
from django.conf import settings
from api.models.token import MyOwnToken

# Django RestFramework
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken

#from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# app
from api.serializers import UsuarioSerializer 
from api.utils import UsuarioUtilidades



User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UsuarioSerializer


class UserAuthToken(ObtainAuthToken):
    """
        Vista para poder relacionar Token con Usuarios
    """
    def getResponseTemplate(self,authentication,message,data):
        return({
            'authentication': authentication,
            'message':message,
            'data': data
        })

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(self.getResponseTemplate(False,"Invalid Credentials",None))
        user = serializer.validated_data['user']
        tokens = UsuarioUtilidades.obtener_token_usuario(user)
        token, created = MyOwnToken.objects.get_or_create(user=user,key=tokens["access_token"])
        response = self.getResponseTemplate(True,"Authentication Succesful",{
            'token': token.key,
            'email': user.email,
            'name': user.nombres,
            'id':str(user.id)
            })
        return Response(response)


