# Generated by Django 4.2.4 on 2023-08-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default-profile-image.jpeg', null=True, upload_to='users/'),
        ),
    ]
