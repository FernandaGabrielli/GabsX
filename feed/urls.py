from django.urls import path
from . import views
from django.urls import path
from .views import like_tweet

urlpatterns = [
    path('', views.home, name = 'home'),
    path('like/<int:tweet_id>/', like_tweet, name='like_tweet'),
]
