from rest_framework import serializers
from .models import Product, ProductImage
from stores.models import Store

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['store', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        store = Store.objects.filter(owner=user).first()
        if not store:
            raise serializers.ValidationError("Sizning do'koningiz yo‘q.")

        validated_data['store'] = store
        return super().create(validated_data)
