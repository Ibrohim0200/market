from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Store
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if instance.owner != request.user:
            raise serializers.ValidationError("Siz bu do'konni o'zgartira olmaysiz.")
        return super().update(instance, validated_data)
