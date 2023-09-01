from django.urls import path
from . import views

urlpatterns = [
    path('addUser/', views.addUser),
    path('currentUser/', views.getUser),
    path('updateUser/', views.updateUser),
    path('uploadUserPhoto/', views.uploadUserPhoto),
    path('getUserPhoto/<str:pk>/', views.getUserPhoto),
    path('deleteUserPhoto/', views.deleteUserPhoto),
    path('deleteUser/', views.deleteUser),
    path('allUsers/', views.getAllUsers),
    path('user/<str:pk>/', views.getOtherUser),
    path('usernames/', views.getAllUsernames),
    path('search/<str:user_name>/', views.searchUser),
]
