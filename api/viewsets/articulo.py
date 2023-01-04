# Python
import json
# Django
from django.http import HttpResponse

# rest_framework
from rest_framework import status, viewsets
from rest_framework.response import Response
from api.utils.service import Fetch

import logging
logger = logging.getLogger(__name__)
# articulo/?page=50&ItemName=MANGUERA
class ArticuloViewSet(viewsets.ReadOnlyModelViewSet):
    select_items = ['ItemName', 'ItemCode', 'U_CodAnterior', 'OnHand', 'Price'] 
    def list(self, request, *args, **kwargs):
        try:
            r = Fetch(path="sap/articulos/pg",params=dict(request.query_params))
            response = r.send()
            messageOcurred = response.get("message",None)
            if messageOcurred is None:
                articulos_sap = [ dict((k, x[k]) for k in self.select_items if k in x) for x in response["items"]]
                response["items"] = articulos_sap
                logger.error("GET ARTICLES")
                return Response(response)
            else:
                return Response(response)
        except Exception as e:
            return Response({"message": e})

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

