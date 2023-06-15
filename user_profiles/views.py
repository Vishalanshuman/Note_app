from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate, login,logout
from .serializers import CreateUserSerializer, LoginSerializer

# Create your views here.

class SignupView(GenericAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def post(self, request:Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response  = {
                "message": "Profile Created Successfully.",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request: Request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = {
                'message': "Login Successfully",
            }


            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        response = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        return Response(data=response, status=status.HTTP_200_OK)
class LogoutView(GenericAPIView):
    def get(self, request:Request):
        logout(request)
        response = {
            "message":"Logout Successfully."
        }
        return Response(data=response, status=status.HTTP_200_OK)