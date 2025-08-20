from django.contrib import admin
from django.urls import path, include
from account.views import RegisterView, LoginView, LoginWithTokenView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/token/', LoginWithTokenView.as_view(), name='login-with-token'),
]