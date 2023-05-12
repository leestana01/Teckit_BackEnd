from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Productfields = (
            'id',
            'product_name',
            'price'
        )