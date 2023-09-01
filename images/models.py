from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from galleries.models import Gallery
import uuid


class Image(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    gallery = models.ForeignKey(
        Gallery, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='galleries/')
    name = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']
