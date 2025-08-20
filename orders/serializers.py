from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user', 'total_price', 'date_of_order']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None

        product = validated_data['product']
        amount = validated_data['amount']

        validated_data['total_price'] = product.price * amount
        validated_data['user'] = user

        return super().create(validated_data)
