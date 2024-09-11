from django.shortcuts import render
from django.contrib.auth.hashers import make_password

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import UsersSerializer
from users.models import Users
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken







##users registration
class UsersListView(APIView):
    def get(self, request):
        users = Users.objects.all()
        name = request.query_params.get("name")
        if name:
            users = users.filter(name=name)
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['password'] = make_password(data['password'])
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersDetailView(APIView):
    def get(self, request, id):
        users = get_object_or_404(Users, id=id)
        serializer = UsersSerializer(users)
        return Response(serializer.data)

    def put(self, request, id):
        users = get_object_or_404(Users, id=id)
        serializer = UsersSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        users = get_object_or_404(Users, id=id)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access':str(refresh.access_token),
                'refresh':str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': f'invalid credentials. Username: {username}, Password: {password}'}, status=status.HTTP_401_UNAUTHORIZED)
   

@csrf_exempt
def generate_token(request):
    user,created =User.objects.get_or_create(username=' ')
    refresh = RefreshToken.for_user(user)
    return JsonResponse({
        'access':str(refresh.access_token),
        'refresh':str(refresh)
    })
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view'}, status=status.HTTP_200_OK)  


