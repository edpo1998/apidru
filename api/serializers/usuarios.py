# models
from django.contrib.auth import get_user_model

# rest_framework
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

class UsuarioReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'nombres',
                  'apellidos', 'email', 'groups', 'user_permissions')
