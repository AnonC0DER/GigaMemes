from genericpath import exists
from django.test import TestCase
from Memes.models import *
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
################################

# Use to access objects in Home views
MEMES_URL = reverse('Home')

class ModelTests(TestCase):
    
    def setUp(self):
        '''Create and authenticate a test user'''
        self.user = User.objects.create_user(username='testuser', password='testpass123@')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
    
    def test_create_new_meme(self):
        '''Test create a new meme'''
        # Create a new meme
        meme = Meme.objects.create(
            owner=self.user.profilemodel,
            title='test',
            text='test text',
            image='Memes/default.jpg'
        )
        
        # Create a get request to return objects
        res = self.client.get(MEMES_URL)
        # If first meme object title equals meme title which I create, the test will pass 
        self.assertEqual(res.context['memes'][0].title, meme.title)

    def test_create_new_tag(self):
        '''Test create a new tag'''
        # Create tag object
        tag = Tag.objects.create(
            name='meme'
        )
        # Filter tag objects
        exists = Tag.objects.filter(
            name=tag.name
        ).exists()
        
        # if the tag was exists it will return True
        self.assertTrue(exists)

    def test_post_comment(self):
        '''Test posting a new comment'''
        # Create a new meme object
        meme = Meme.objects.create(
            owner=self.user.profilemodel,
            title='test',
            text='test text',
            image='Memes/default.jpg'
        )
        # Create a new comment object
        comment = Comment.objects.create(
            body='Good',
            meme=meme,
            owner=self.user.profilemodel,
        )
        # Filter comment objects
        exists = Comment.objects.filter(
            id=comment.id
        ).exists()

        # if the comment was exists it will return True
        self.assertTrue(exists)
    
    def test_post_comment(self):
        '''Test posting a new vote'''
        # Create a new meme object
        meme = Meme.objects.create(
            owner=self.user.profilemodel,
            title='test',
            text='test text',
            image='Memes/default.jpg'
        )
        # Create a new vote object
        vote = Vote.objects.create(
            vote='up',
            meme=meme,
            owner=self.user.profilemodel,
        )
        # Filter vote objects
        exists = Vote.objects.filter(
            id=vote.id
        ).exists()

        # if the vote was exists it will return True
        self.assertTrue(exists)