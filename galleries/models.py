from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
import uuid
# Create your models here.


class Gallery(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    privacy = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    imagesCount = models.BigIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']
