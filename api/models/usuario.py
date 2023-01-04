# Django
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from api.models import ModeloBase
from django.conf import settings




class CustomUserManager(UserManager):
    """
        Modelo que para custumizar los usuarios de Django
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('El email es requerido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class Usuario(ModeloBase, AbstractUser):
    """
    Modelo que se utilizara como AUTH_USER_MODEL en el proyecto.
    Esta clase provee a todos los modelos de los siguientes atributos:
        + username       (CharField)  Nombre de usuario
        + nombres        (datetime)  Nombres en conjunto
        + apellidos      (datetime)  Apellidos en conjunto
        + email          (datetime)  Email del Usuario
        + first_name     (datetime)  Primer nombre del Usuario
        + last_name      (datetime)  Ultimo apellido del Usuario
        + activo         (datetime)  Estado del Registro 
        + objects        (Usuario)  Objecto al que esta realcionado el modelo del Usuario de Django
    """
    username = models.CharField(max_length=150, null=True, blank=True)
    nombres = models.CharField(max_length=150, null=True, blank=True)
    apellidos = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)

    first_name = None
    last_name = None
    activo = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombres']
    objects = CustomUserManager()

    def __str__(self):
        return '{} - {}'.format(self.id, self.nombres)

    @property
    def get_nombre(self):
        return '{}'.format(self.nombres)

    def delete(self, *args):
        self.email = f"{self.email}--{timezone.now()}"
        self.activo = False
        self.save()
        return True


