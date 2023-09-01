from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


def home(request):
    return HttpResponse('Welcome to the Backend of Pixaroom Gallery application')


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/galleries/', include('galleries.urls')),
    path('api/images/', include('images.urls')),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
