from rest_framework import serializers
from .models import CardOfUsers

class CardOfUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardOfUsers
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
