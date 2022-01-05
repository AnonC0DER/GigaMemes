# Why we use Signals in Django?
'''
** signals.py doesn't work if the configuration of app.py is not correct **

Example for why we use Signals : We have a website and users can register and login in our website
every time a user registered we wanna send a welcome email to the user
in this situation we use signals.
Signals are just a way of to listening to actions in our application.

REF : https://docs.djangoproject.com/en/4.0/topics/signals/
'''

# post_save : anytime a model is saved (after it saved)
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
################################
'''
Instead of @receiver(post_save, sender=User),
we can use post_delete.connect(ProfileDeletedSignal, sender=Profile) and post_save.connect(ProfileUpdatedSignal, sender=Profile)
'''


# Create Profile
@receiver(post_save, sender=User)
def CreateProfileSignal(sender, instance, created, **kwargs):
    '''
    What does this function do? This function create a profile immediately after the user is generated.

    sender == Users.models.Profile,
    instance == user.username
    created returns False or True.
    if it returns True, it means this is the first time this user created
    and if it returns False, it means the user is not new. 
    
    print(instance)
    print(sender)
    print(created)
    '''

    if created:
        user = instance
        # create profile
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
    


# Delete User
@receiver(post_delete, sender=Profile)
def ProfileDeletedSignal(sender, instance, **kwargs):
    '''
    What does this function do? If admin delete the profile, this function will delete the user, too.

    sender == Users.models.Profile,
    instance == user.username

    print(instance)
    print(sender)
    '''
    
    try:
        user = instance.user
        user.delete()
    except:
        pass


# Hesam Norin