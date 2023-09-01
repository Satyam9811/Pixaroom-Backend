# Generated by Django 4.2.4 on 2023-08-13 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_name_profile_first_name_profile_last_name'),
        ('galleries', '0003_remove_gallery_profile_gallery_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='userId',
        ),
        migrations.AddField(
            model_name='gallery',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]