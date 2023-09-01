from rest_framework import serializers
from .models import Gallery
from images.models import Image
from images.serializers import ImageSerializer


class GallerySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = '__all__'
        # fields = ['id', 'name', 'privacy']

    def get_images(self, obj):
        images = obj.image_set.all()
        serializer = ImageSerializer(images, many=True)
        return serializer.data
