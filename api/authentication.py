from rest_framework.authentication import TokenAuthentication
from .models import MyOwnToken

class MyOwnTokenAuthentication(TokenAuthentication):
    model = MyOwnToken