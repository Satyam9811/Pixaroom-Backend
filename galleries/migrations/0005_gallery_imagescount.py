# Generated by Django 4.2.4 on 2023-08-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0004_remove_gallery_userid_gallery_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='imagesCount',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]