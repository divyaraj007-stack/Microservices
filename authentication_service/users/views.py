import requests
from rest_framework import viewsets, status, decorators
from rest_framework.response import Response
from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class UserAuthViewSet(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = []

    @decorators.action(methods=["POST"], detail=False)
    def sign_up(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @decorators.action(methods=["POST"], detail=False)
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @decorators.action(detail=False)
    def product_list(self, request, *args, **kwargs):
        url = "http://127.0.0.1:8001/products/"
        response = requests.get(url, headers={"X-Header": "product-service"})

        if response.status_code in [200, 400, 403, 401, 404]:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @decorators.action(methods=["POST"], detail=False)
    def create_order(self, request, *args, **kwargs):
        url = "http://127.0.0.1:8002/orders/"
        response = requests.post(url, headers={"X-Header": "order-service"}, json=request.data)

        if response.status_code in [200, 201, 400, 403, 401, 404]:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_400_BAD_REQUEST)