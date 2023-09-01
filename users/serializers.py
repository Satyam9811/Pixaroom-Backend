from rest_framework import serializers
from .models import Profile
from galleries.models import Gallery
from galleries.serializers import GallerySerializer


class ProfileSerializer(serializers.ModelSerializer):
    galleries = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = '__all__'

    def get_galleries(self, obj):
        galleries = obj.gallery_set.all()
        serializer = GallerySerializer(galleries, many=True)
        return serializer.data
