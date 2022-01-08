from rest_framework.serializers import (
    ModelSerializer, SerializerMethodField,
    CharField, ValidationError
)
from Memes.models import Tag, Comment, Vote, Meme
from Users.models import ProfileModel
from django.contrib.auth.models import User
#################################################

# Profile serializer
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'


# Tags serializer
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# Comment serializer
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# Vote serializer
class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


# Meme serializer
class MemeSerializer(ModelSerializer):
    '''
    If we don't use owner, tags, votes and comments
    we can only get owner, tag, votes or comments ID. So if we want to
    access to objects, we should use them. 

    votes and comments -> this variables get their values by calling get_votes() and get_comments() methods, 
    They can be used to add any sort of data to the serialized representation of our objects.
    Ref : https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    '''
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    votes = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        '''
        We can customize our fields, too.
        Just like this, fields = ['title', ...]
        '''
        model = Meme
        fields = '__all__'


    # Get votes
    ## We always have to start our method with get
    def get_votes(self, meme):                  # self refer to serializer class
        # vote_set is how we get models children, it must be in lower case
        votes = meme.vote_set.all()
        serializer = VoteSerializer(votes, many=True)
        return serializer.data

    # Get comments
    def get_comments(self, meme):
        comments = meme.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data 


# Registration model
class RegistrationSerializer(ModelSerializer):

    # Passwords must be write_only, user cannot read it
    password = CharField(style={'input_type' : 'password'}, write_only=True)
    password2 = CharField(style={'input_type' : 'password'}, write_only=True)
    
    class Meta:
        '''
        https://www.django-rest-framework.org/api-guide/serializers/#listserializer
        '''
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password' : {
                'write_only' : True, 
                'min_length' : 5
            }
        }


    def validate(self, attrs):
        '''
        Stop duplicate emails
        
        REF : https://www.django-rest-framework.org/api-guide/validators/#updating-nested-serializers
        '''
        
        email = attrs.get('email')
        # Check the given email address is already in database
        if User.objects.filter(email=email):
            raise ValidationError({
                'duplicate_email' : 'The given email is already registered !'
            }) 

        return attrs


    def save(self):
        '''
        We override save() method because we need to make sure two passwords match.

        validated_data -> Returns the validated incoming data
        '''

        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            
        )
        # Get passwords values to check them
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        # Check passwords match
        if password != password2:
            raise ValidationError({
                'password_error' : 'Passwords must match !'
            })
        
        # if the passwords match, set the password
        user.set_password(password)
        user.save()

        return user
    

# Create new meme
class CreateMemeSerializer(ModelSerializer):
    class Meta:
        model = Meme
        fields = ['title', 'text', 'image', 'tags']



