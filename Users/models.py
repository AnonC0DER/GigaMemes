from django.db import models
from django.contrib.auth.models import User
import uuid
###########################################

# Profile model
class Profile(models.Model):
    '''
    Profile model. \n
    Using Django User model. \n

    unique=True, primary_key=True -> Make sure to don't create a meme with an id that already taken.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    bio = models.TextField(max_length=250, default="Hey there, I'm using GigaMemes !")
    reddit_account = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(upload_to='Profiles/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Return username
    # In case that the user doesn't exists we make self.username string, if the user doesn't exists it returns None 
    def __str__(self):
        return str(self.username)

    # We use this property in frontend instead of profile_image, so if user deleted image, it doesn't break page
    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = '/images/Profiles/default.jpg'

        return url
    