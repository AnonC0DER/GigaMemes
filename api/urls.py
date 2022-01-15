from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
###################


urlpatterns = [
    path('', views.GetUrlsPaths),
    path('docs/', include_docs_urls(title='GigaAPIs-docs')),
    path('memes/', views.GetMemes),
    path('single-meme/<str:pk>/', views.GetSingleMeme),
    
    path('search-meme/', views.SearchMemes),
    path('vote-meme/<str:pk>/', views.VotesView),
    path('comment-meme/<str:pk>/', views.CommentsView),
    path('create-meme/', views.CreateMemeView.as_view()),
    path('create-tag/', views.CreateTagView.as_view()),

    path('users/register/', views.RegistrationUserView.as_view()),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('schema/', get_schema_view(
        title='GigaMemes-schema',
        description='GigaMemes-schema',
        version='1.0.0'
    ), name='openapi-schema'),

    path('check-jwt/', views.CheckJWT)
]