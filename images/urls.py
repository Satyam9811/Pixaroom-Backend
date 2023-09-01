from django.urls import path
from . import views

urlpatterns = [
    path('addImages/<str:pk>/', views.addImages),
    path('deleteImage/<str:pk>/', views.deleteImage),
    path('deleteAllImages/<str:pk>/', views.deleteAllImages),
]
