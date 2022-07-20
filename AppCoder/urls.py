from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio),
]