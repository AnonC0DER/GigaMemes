from django.db import models
from django.db.models.base import Model
from Users.models import Profile
import uuid
############################

# Memes model
class Meme(models.Model):
    '''
    Meme Model. \n
    imageURL property :
        - Use this in frontend instead of profile_image variable, so if the user deleted profile_image, it doesn't break page \n
    
    votes property :
        - Return a list of all users IDs voted on the meme
    
    comments property :
        - Return a list of all users IDs commented on the meme
    
    getVoteCount property :
        - Get all votes and count them, filter up votes and count them. Save new data to votes_total and votes_ratio variables

    We don't wanna get the objects, we want to get the owner id, so use values_list(), flat=True -> return list of IDs. \n
    If users aren't log in, they can't vote or they can't comment. Users only can vote one time per memes.
    '''
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=220)
    text = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag') 
    image = models.ImageField(upload_to='Memes/')
    votes_total = models.IntegerField(default=0, null=True, blank=True)
    votes_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Return title
    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-created']


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/images/Profiles/default.jpg'

        # return user's profile image url or default user profile image
        return url 
    

    @property
    def votes(self):
        ## 
        queryset = self.vote_set.all().values_list('owner__id', flat=True)
        return queryset
    
    
    @property
    def comments(self):
        queryset = self.comment_set.all().values_list('owner__id', flat=True)
        return queryset


    @property
    def getVoteCount(self):
        # get all the votes
        votes = self.vote_set.all()
        # filter up votes and count all of them
        upVotes = votes.filter(vote='up').count()
        # count all votes
        totalVotes = votes.count()

        # count the ratio
        ## get all up votes and divide them by total votes, then multiply it to 100 to get the ratio
        ratio = (upVotes / totalVotes) * 100
        # set new data
        self.votes_ratio = ratio
        self.votes_total = totalVotes
        # save all data
        self.save()



# Tags model
class Tag(models.Model):
    '''
    Tags model. \n
    unique=True, primary_key=True -> Make sure to don't create a meme with an id that already taken.
    '''
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # return name
    def __str__(self):
        return self.name





# Vote Model
class Vote(models.Model):
    '''
    Vote model. \n
    Add new values to VOTE_TYPE. \n
    up -> Input value, Up vote -> Output value \n

    unique=True, primary_key=True -> Make sure to don't create a meme with an id that already taken.
    '''
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    vote = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Users can only leave one vote per meme
    class Meta:
        unique_together = [['owner', 'meme']]

    # return vote
    def __str__(self):
        return self.vote



# Comment Model
class Comment(models.Model):
    '''
    Comment Model. \n

    unique=True, primary_key=True -> Make sure to don't create a meme with an id that already taken.
    '''
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)
    body = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.owner__name



# Hesam Norin