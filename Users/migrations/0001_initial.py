# Generated by Django 3.2.9 on 2022-01-04 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('bio', models.TextField(default="Hey there, I'm using GigaMemes !", max_length=250)),
                ('reddit_account', models.CharField(max_length=200)),
                ('profile_image', models.ImageField(upload_to='Profiles/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
