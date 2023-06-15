from django.contrib.auth.models import User
from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password'] 

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300)
    password = serializers.CharField(max_length=300)

    class Meta:
        fields = ['username', 'password']