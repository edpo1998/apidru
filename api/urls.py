from django.urls import path, include
from rest_framework import routers
from api import viewsets
from django.conf import settings
router = routers.DefaultRouter()

# Home
router.register(r'home', viewsets.HomeViewSet,
                basename="home")

# Usuario
router.register(r'user', viewsets.UserViewSet, 
                basename='usuario')

# Articulo
router.register(r'articulo',viewsets.ArticuloViewSet,
                basename="articulo")

# URL patterns
urlpatterns = [
    path(f'{settings.VERSION_API}/', include(router.urls)),
    path(f'{settings.VERSION_API}/auth/',viewsets.UserAuthToken.as_view()),
]
