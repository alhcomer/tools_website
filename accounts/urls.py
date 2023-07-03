from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('auth/', include("django.contrib.auth.urls"), name='auth')
]
