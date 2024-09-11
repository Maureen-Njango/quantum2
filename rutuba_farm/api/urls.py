
from django.contrib import admin
from django.urls import path

from .import views
from django.urls import path
from api.views import LoginView  
from .views import generate_token , ProtectedView
from .views import UsersListView
from .views import UsersDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView





urlpatterns = [
    # path('admin/', admin.site.urls),
    
    # path('generate_token', include('generate_token.urls')),
    path('users/', UsersListView.as_view(), name='users_list_view'),
    path('users/<int:id>/', UsersDetailView.as_view(), name='users_detail_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('generate_token/', views.generate_token, name='generate_token'),
    path('protected/', ProtectedView.as_view(), name='protected_view'),

    
    
]

