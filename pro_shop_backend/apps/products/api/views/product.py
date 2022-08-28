from rest_framework.pagination import PageNumberPagination
from rest_access_policy import AccessPolicy
from rest_framework import viewsets, status
from rest_framework.response import Response
from pro_shop_backend.apps.products.api.serializers.product import ListSerializer
from pro_shop_backend.apps.products.models import Product


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        stores = Product.objects.all()
        serializer = ListSerializer(stores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        if not pk:
            return Response("No se encontro el pk", status=status.HTTP_404_NOT_FOUND)
        store = Product.objects.get(_id=pk)
        if not store:
            return Response("No existe el product", status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)
