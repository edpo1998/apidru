# Django Models
from django.db import models


class ModeloBase(models.Model):
    """
    Modelo abstracto base para el resto de modelos.
    Esta clase provee a todos los modelos de los siguientes atributos:
        + activo       (boolean)   Si el registro está o no anulado.
        + creado       (datetime)  La fecha de creación del registro.
        + modificado   (datetime)  La fecha de la última actualización del registro.
        + CreatedBy   (Usuario)   El usuario que creó el registro.
        + UpdatedBy  (Usuario)   El usuario que actualizó el registro.
    """
    activo = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    createdBy = models.CharField(max_length=150, default='unknown')
    updatedBy = models.CharField(max_length=150, default='unknown')

    def __index__(self):
        return id

    class Meta:
        """ Opciones adicionales. """
        abstract = True
        ordering = ['id']

    def delete(self, *args):
        self.activo = False
        self.save()
        return True

    def hard_delete(self, *args, **kwargs):
        super(ModeloBase, self).delete(*args, **kwargs)
