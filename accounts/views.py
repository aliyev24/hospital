from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate
from rest_framework import status


from .tokens import create_jwt_pair_for_user
from . import serializers


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer


class SignUpView(GenericAPIView):
    serializer_class = serializers.SignUpSerializer

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User Created Successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):

    def post(self, request: Request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {"message": "Login Successfull", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)
