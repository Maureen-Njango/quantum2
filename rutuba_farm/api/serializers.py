from rest_framework import serializers
from users.models import Users
from django.contrib.auth.models import User





class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields="__all__"
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)        