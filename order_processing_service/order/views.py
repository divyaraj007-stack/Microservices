from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from order_processing_service.permissions import *

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AuthServicePermission]
    authentication_classes = []
    http_method_names = [
        "get",
        "post",
        "put",
        "delete",
    ]