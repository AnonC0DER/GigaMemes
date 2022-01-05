from django.shortcuts import render
from .models import Meme
###################################

# All memes
def MemesViews(request):
    # Test views
    memes = Meme.objects.all()
    context = {'memes' : memes}
    return render(request, 'Memes/home.html', context)


def SingleMemeViews(request):
    pass











# Hesam Norin