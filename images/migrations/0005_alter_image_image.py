# Generated by Django 4.2.4 on 2023-08-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='users/default-profile-image.png', null=True, upload_to='galleries/'),
        ),
    ]