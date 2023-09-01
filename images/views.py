from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import Image
from galleries.models import Gallery
from users.models import Profile
import os


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addImages(request, pk):
    images = request.FILES.getlist('images')
    gallery = Gallery.objects.get(id=pk)
    profile = Profile.objects.get(id=request.user.profile.id)
    for image in images:
        Image.objects.create(profile=profile, gallery=gallery,
                             image=image, name=image.name)

    profile.imagesCount += len(images)
    profile.save()
    gallery.imagesCount += len(images)
    gallery.save()
    return Response('photos were added successfully')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteImage(request, pk):
    profile = Profile.objects.get(id=request.user.profile.id)
    profile.imagesCount -= 1
    profile.save()
    image = Image.objects.get(id=pk)
    gallery = Gallery.objects.get(id=image.gallery.id)
    gallery.imagesCount -= 1
    gallery.save()
    if os.path.exists(image.image.path):
        os.remove(image.image.path)
    image.delete()
    return Response('gallery photo deleted successfully')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteAllImages(request, pk):
    profile = Profile.objects.get(id=request.user.profile.id)
    gallery = Gallery.objects.get(id=pk)
    profile.imagesCount -= gallery.imagesCount
    profile.save()
    images = gallery.image_set.all()
    for image in images:
        if os.path.exists(image.image.path):
            os.remove(image.image.path)
        image.delete()
    gallery.imagesCount = 0
    gallery.save()
    return Response('All images from gallery were deleted successfully')
