from django.contrib import admin
from api.models import  MyOwnToken , Usuario
"""
    Registro de modelos para poder configurarlos en 
    el panel de administracion de Django
"""
class TokenAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

class UsuarioAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

admin.site.register(MyOwnToken,TokenAdmin)
admin.site.register(Usuario,UsuarioAdmin)
