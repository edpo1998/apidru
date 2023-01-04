
# django
from django.conf import settings

# rest_framework
from rest_framework.exceptions import PermissionDenied

# JWt Token
from rest_framework_simplejwt.tokens import RefreshToken

# Otros
#import requests as req
from json.decoder import JSONDecodeError


class UsuarioUtilidades:
    """Utilidades que serviran para el registro y autenticarían del usuario"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def obtener_token_usuario(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }
