# Generated by Django 3.2.9 on 2022-01-05 19:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Memes', '0002_auto_20220105_0009'),
        ('Users', '0002_auto_20220105_0030'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='ProfileModel',
        ),
    ]
