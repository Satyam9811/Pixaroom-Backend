from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save, sender=Profile)


# def createProfile(sender, instance, created, **kwargs):
#     if created:
#         user = instance
#         profile = Profile.objects.create(
#             user=user,
#             username=user.username,
#             email=user.email,
#         )


def createUser(sender, instance, created, **kwargs):
    if created:
        profile = instance
        user = User.objects.create_user(
            profile.username, profile.email, profile.password
        )
        profile.user = user
        # print(user.password)
        profile.save()

        subject = 'Welcome to Pixaroom'
        message = 'We are glad you signed up on our platform! Have a happy time!!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        if profile.first_name:
            user.first_name = profile.first_name
        if profile.last_name:
            user.last_name = profile.last_name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()

        # subject = 'Pixaroom account deleted'
        # message = 'We have successfully deleted your Pixaroom account. We are glad you used our service. Hoping for you to come back soon!'

        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [instance.email],
        #     fail_silently=False
        # )

    except:
        pass


# post_save.connect(createProfile, sender=User)
post_save.connect(createUser, sender=Profile)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
