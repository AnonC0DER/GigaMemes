from django.contrib import admin
from .models import Meme, Tag, Vote, Comment

# Register your models here.
admin.site.register(Meme)
admin.site.register(Tag)
admin.site.register(Vote)
admin.site.register(Comment)