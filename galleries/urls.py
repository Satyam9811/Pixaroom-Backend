from django.urls import path
from . import views

urlpatterns = [
    path('addGallery/', views.addGallery),
    path('get/<str:userId>/<str:pk>/', views.getGallery),
    path('updateGallery/', views.updateGallery),
    path('deleteGallery/<str:pk>/', views.deleteGallery),
    path('deleteAllGalleries/', views.deleteAllGalleries),
    path('gallerynames/<str:pk>/', views.getAllGalleryNames),
    path('search/<str:gallery_name>/<str:pk>/', views.searchGallery),
]
