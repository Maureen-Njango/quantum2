from rest_framework import serializers
from users.models import Users





class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields="__all__"
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)        