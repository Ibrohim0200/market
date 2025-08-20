from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from account.models import User
from .utils import create_token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'role', 'address', 'phone', 'token']
        read_only_fields = ['token', 'role']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise ValidationError("Email yoki parol noto‘g‘ri")
        if not user.is_active:
            raise ValidationError('Foydalanuvchi faol emas')
        return {"user": user}

class UserCreateSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 're_password', 'address', 'phone', 'role']
        extra_kwargs = {
            'password': {"write_only": True}
        }

    def validate(self, data):
        re_password = data.pop("re_password")
        password = data.get("password")

        if password != re_password:
            raise ValidationError("Parollar mos kelmaydi")

        request = self.context.get('request')
        if data.get('role') == 'admin':
            if not request.user.is_authenticated or not request.user.is_superuser:
                data['role'] = 'user'

        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class LoginWithTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise ValidationError("Email yoki parol noto‘g‘ri")
        if not user.is_active:
            raise ValidationError("Foydalanuvchi faol emas")

        token = create_token(user.id)
        return {
            "access_token": token.get("access_token"),
            "refresh_token": token.get("refresh_token")
        }
    