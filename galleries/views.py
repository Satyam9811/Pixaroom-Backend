from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import GallerySerializer
from .models import Gallery
from users.models import Profile
import os


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addGallery(request):
    print(request.user.profile.id)
    data = request.data
    name = data['name']
    privacy = data['privacy']

    name_exist = Gallery.objects.filter(name=name).exists()

    if not name_exist:
        gallery = Gallery.objects.create(
            name=name,
            privacy=privacy
        )
        profile = Profile.objects.get(id=request.user.profile.id)
        profile.galleriesCount += 1
        profile.save()
        gallery.profile = profile
        gallery.save()
    else:
        return Response('gallery name already exists!', status=400)

    return Response('gallery was created successfully')


# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def getGallery(request, userId, pk):
    # userId = request.user.profile.id
    try:
        gallery = Gallery.objects.get(id=pk)
    except:
        gallery = None

    if gallery is None:
        return Response("Gallery does not exist", status=404)

    if userId == str(gallery.profile.id) or gallery.privacy == 'public':
        serializer = GallerySerializer(gallery, many=False)
        return Response(serializer.data)

    return Response("Gallery does not exist", status=404)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateGallery(request):
    data = request.data
    print(data)
    id = data['id']
    name = data['name']
    privacy = data['privacy']
    gallery = Gallery.objects.get(id=id)

    if gallery.name != name:
        try:
            g = Gallery.objects.get(name=name)
        except:
            g = None

        if g is not None:
            return Response('gallery name already exists!', status=403)

    gallery.name = name
    gallery.privacy = privacy
    gallery.save()
    return Response('gallery details were updated successfully')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteGallery(request, pk):
    gallery = Gallery.objects.get(id=pk)
    if gallery.profile.id != request.user.profile.id:
        return Response('Not authorized to delete the gallery')

    profile = Profile.objects.get(id=request.user.profile.id)
    profile.galleriesCount -= 1
    profile.imagesCount -= gallery.imagesCount
    profile.save()
    images = gallery.image_set.all()
    for image in images:
        if os.path.exists(image.image.path):
            os.remove(image.image.path)

    gallery.delete()
    return Response('Gallery was deleted successfully')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteAllGalleries(request):
    galleries = Gallery.objects.filter(profile=request.user.profile)
    galleries.delete()
    profile = Profile.objects.get(id=request.user.profile.id)
    profile.galleriesCount = 0
    profile.save()
    return Response('All galleries were deleted successfully')


@api_view(['GET'])
def getAllGalleryNames(request, pk):
    galleries = Gallery.objects.all()
    gallerynames = []
    for gallery in galleries:
        if gallery.privacy == 'public':
            gallerynames.append(gallery.name)
        else:
            if str(gallery.profile.id) == pk:
                gallerynames.append(gallery.name)

    return Response(gallerynames)


@api_view(['GET'])
def searchGallery(request, gallery_name, pk):
    try:
        gallery = Gallery.objects.get(name=gallery_name)
    except:
        return Response('Not found')
    if gallery.privacy == 'private':
        if str(gallery.profile.id) != pk:
            return Response('Not found')

    return Response(gallery.id)
