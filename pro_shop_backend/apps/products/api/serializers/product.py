from rest_framework import serializers
from pro_shop_backend.apps.products.models import Product


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "_id",
            "name",
            "brand",
            "category",
            "description",
            "rating",
            "numReviews",
            "price",
            "countInStock",
            "createdAt",
            "_id",
        ]
