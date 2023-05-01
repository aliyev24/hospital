from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username", "password"]

    def validate(self, attrs):

        email_exists = CustomUser.objects.filter(
            username=attrs["username"]
        ).exists()

        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        from rest_framework.authtoken import models
        user.save()
        models.Token.objects.create(user=user)
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
