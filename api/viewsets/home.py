# Django
from django.http import HttpResponse

# rest_framework
from rest_framework import status, viewsets
from rest_framework.response import Response

#logger
import logging
logger = logging.getLogger(__name__)
class HomeViewSet(viewsets.ReadOnlyModelViewSet):

    def list(self, request, *args, **kwargs):
        logger.error("HOLA",exc_info=True)
        return Response({'message':"API RUNNING..."})

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
