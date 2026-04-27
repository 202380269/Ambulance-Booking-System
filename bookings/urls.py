from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
     path('book/', views.create_booking, name='create_booking'),
    path('register/', views.register_view, name='register'),
]