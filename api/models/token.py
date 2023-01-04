# Python
import binascii
import os

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth import get_user_model

class MyOwnToken(models.Model):
    """
    Modelo Token para la authenticacion y relacion con el Usuario Customizado, no se utiliza el de DRF.
    Esta clase provee a todos los modelos de los siguientes atributos:
        + key       (CharField)   Token generado para el usuario.
        + created       (datetime)  Fecha en que se creo el token.
        + user   (Usuario)  Usuario al que esta relacionado el token.
    """
    key = models.CharField(_("Key"), max_length=2048, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("Usuario")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(MyOwnToken, self).save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
