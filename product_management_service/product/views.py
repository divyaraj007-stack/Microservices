from rest_framework import viewsets
from .models import Product
from product_management_service.permissions import *
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AuthServicePermission]
    authentication_classes = []
    http_method_names = [
        "get",
        "post",
        "put",
        "delete",
    ]
