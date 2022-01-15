from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from Memes.models import Meme, Tag, Vote, Comment
from rest_framework import generics

from api import serializers
###################################

# Return all urls path
@api_view(['GET'])
def GetUrlsPaths(request):
    '''
    All URLs. \n\n
    ** By Hesam Norin ** \n
    '''
    URLs = {
        'GET' : {
            'Get all memes objects' : '/api/memes/',
            'Get one meme object' : '/api/single-meme/ID/',
        },
        'POST' : {
            'Search memes' : '/api/search-meme/',
            'Search memes' : '/api/search-meme/',
            'Comment memes' : '/api/comment-meme/',
            'Vote memes' : '/api/vote-meme/',
            'Register new user' : '/api/users/register/',
        }
    }

    return Response(URLs)


# Return all memes objects
@api_view(['GET'])
def GetMemes(request):
    '''
    Return all memes objects. \n
    Use this to get single object : /api/single-meme/ID/ 
    '''
    memes = Meme.objects.all()
    # many=True -> return more than one object
    serializer = MemeSerializer(memes, many=True)

    return Response(serializer.data)


# Get meme object
@api_view(['GET'])
# Only authenticated users can use this service
@permission_classes([IsAuthenticated])
def GetSingleMeme(request, pk):
    meme = Meme.objects.get(id=pk)
    # many=False -> return one object
    serializer = MemeSerializer(meme, many=False)

    return Response(serializer.data)


# Search Memes
@api_view(['POST'])
# Only authenticated users can use this service
@permission_classes([IsAuthenticated])
def SearchMemes(request):
    # Get data
    data = request.data
    # Save the query
    query = data['query']

    # Filter tags by name, icontains : Case-insensitive containment test
    tags = Tag.objects.filter(
        name__icontains = query
    )

    '''
    Filter all resumes by title, description, owner name, 
    tags, experience level name and stack name

    Keyword argument queries – in filter(), etc. – are “AND”ed together. 
    If we need to execute more complex queries 
    (for example, queries with OR statements), you can use Q objects.
    
    distinct() Returns a new QuerySet that uses SELECT DISTINCT in its SQL query.
    This eliminates duplicate rows from the query results. 
    By default, a QuerySet will not eliminate duplicate rows.

    Ref : https://docs.djangoproject.com/en/4.0/topics/db/queries/#complex-lookups-with-q-objects
    '''

    memes = Meme.objects.distinct().filter(
        Q(title__icontains = query) |
        Q(text__icontains = query) |
        Q(owner__name__icontains=query) |
        Q(tags__in = tags)
    )

    # many=True -> there are more than one resume
    serializer = MemeSerializer(memes, many=True)
    return Response(serializer.data)


# Votes
@api_view(['POST'])
# Only authenticated users can use this service
@permission_classes([IsAuthenticated])
def VotesView(request, pk):
    '''
    ### You must authenticate to use this service. <br>
    Only POST method is available. <br>
    <br>
    You can get user jwt (JSON web tokens) authentication in /api/users/token/
    <br>
    '''
    # Get the meme object
    meme = Meme.objects.get(id=pk)
    # Get the user profile
    user = request.user.profilemodel
    # Get the data
    data = request.data

    # if user.id is in meme.votes, that means the user has already submitted his vote
    # you can find votes property in Memes.models, Meme model, line 56
    if user.id in meme.votes:
        return Response({'AlreadyError' : 'You have already submitted your vote for this meme'})
    
    # if user hsan't submitted any vote :
    else:
        vote, created = Vote.objects.get_or_create(
            owner = user,
            meme = meme
        )

        # Save the data
        vote.vote = data['vote']
        vote.save()
        # get vote count from getVoteCount property, Memes.models, Meme model, line 65
        meme.getVoteCount

        serializer = MemeSerializer(meme, many=False)
        return Response(serializer.data)

    
# Comments
@api_view(['POST'])
# Only authenticated users can use this service
@permission_classes([IsAuthenticated])
def CommentsView(request, pk):
    '''
    ### You must authenticate to use this service. <br>
    Only POST method is available. <br>
    <br>
    You can get user jwt (JSON web tokens) authentication in /api/users/token/
    <br>
    '''

    # Get meme object
    meme = Meme.objects.get(id=pk)
    # Get user profile
    user = request.user.profilemodel
    # Get data
    data = request.data

    # Create or get the object
    comment, created = Comment.objects.get_or_create(
        owner = user,
        meme = meme
    )

    # Save the data
    comment.body = data['body']
    comment.save()
    # Get vote count from getVoteCount property, Memes.models, Meme model, line 65
    meme.getVoteCount

    serializer = MemeSerializer(meme, many=False)
    return Response(serializer.data)


# Register new user (class based-views)
class RegistrationUserView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


# Create new meme
# Only authenticated users can use this service
class CreateMemeView(generics.CreateAPIView):
    '''
    Only POST method is available. \n
    Use this link to create new tag : **/api/create-tag/**
    '''
    serializer_class = CreateMemeSerializer
    permission_classes = (IsAuthenticated, )


# Create new tag
# Only authenticated users can use this service
class CreateTagView(generics.CreateAPIView):
    '''
    Only POST method is available. \n
    Use this link to create new meme : **/api/create-meme/**
    '''
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated, )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CheckJWT(request):
    '''Check JSON web token'''

    return Response({'IsAuthenticated' : 'True'})
