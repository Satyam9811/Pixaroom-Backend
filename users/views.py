from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProfileSerializer
from .models import Profile
from django.core.files.base import ContentFile
import base64
import os


@api_view(['POST'])
def addUser(request):
    data = request.data
    username = data['username']
    email = data['email']
    password = data['password']
    print(data)

    username_exist = Profile.objects.filter(username=username).exists()
    email_exist = Profile.objects.filter(email=email).exists()

    if not username_exist and not email_exist:
        Profile.objects.create(
            username=username,
            email=email,
            password=password
        )
    elif not username_exist:
        return Response('email already exists!', status=400)
    elif not email_exist:
        return Response('username already exists!', status=400)
    else:
        return Response('username and email already exists!', status=400)

    # try:
    # user = User.objects.create_user(username, email, password)
    # except:
    # return Response('user already exists!', status=400)

    return Response('user was added successfully')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    profile = request.user.profile
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getAllUsers(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getOtherUser(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request):
    profile = request.user.profile
    data = request.data
    # print(request.data)

    if 'firstName' in data:
        profile.first_name = data['firstName']

    if 'lastName' in data:
        profile.last_name = data['lastName']

    if 'bio' in data:
        profile.bio = data['bio']

    if 'email' in data:
        try:
            user = Profile.objects.get(email=data['email'])
        except:
            user = None

        if user is not None:
            if user.id != profile.id:
                return Response('email already exists!', status=403)

        profile.email = data['email']

    if 'image' in data:
        profile.profile_image = data['image']

    profile.save()
    return Response('user details were updated successfully')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uploadUserPhoto(request):
    profile = request.user.profile
    image = request.FILES.get('image')
    user = Profile.objects.get(id=profile.id)

    # file_data = ContentFile(base64.b64decode(image))
    # object.file.save(file_name, file_data)
    # user.profile_image = file_data

    user.profile_image = image
    user.save()
    return Response('user photo added successfully')


@api_view(['GET'])
def getUserPhoto(request, pk):
    user = Profile.objects.get(id=pk)
    # photo = user.profile_image.url
    try:
        photo = request.build_absolute_uri(user.profile_image.url)
    except:
        photo = None
    return Response(photo)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUserPhoto(request):
    profile = request.user.profile
    user = Profile.objects.get(id=profile.id)
    if os.path.exists(user.profile_image.path):
        os.remove(user.profile_image.path)
    user.profile_image = None
    user.save()
    return Response('user photo deleted successfully')


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUser(request):
    profile = Profile.objects.get(id=request.user.profile.id)
    galleries = profile.gallery_set.all()
    for gallery in galleries:
        images = gallery.image_set.all()
        for image in images:
            if os.path.exists(image.image.path):
                os.remove(image.image.path)

    # os.remove(profile.profile_image.path)
    profile.delete()
    return Response('user was deleted successfully')


@api_view(['GET'])
def getAllUsernames(request):
    profiles = Profile.objects.all()
    # usernames = []
    # for profile in profiles:
    #     usernames.append(profile.username)
    usernames = [profile.username for profile in profiles]
    return Response(usernames)


@api_view(['GET'])
def searchUser(request, user_name):
    try:
        profile = Profile.objects.get(username=user_name)
    except:
        return Response('Not found')
    return Response(profile.id)
