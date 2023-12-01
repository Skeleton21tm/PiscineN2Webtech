from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, ma_vue_protegee

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('ma_vue_protegee/', ma_vue_protegee, name='ma_vue_protegee'),
    
]