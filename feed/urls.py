from django.urls import path
from .views import TweetListView, user_tweets, like_tweet

urlpatterns = [
    path('', TweetListView.as_view(), name='home'),  # URL para a lista de tweets
    path('user/tweets/', user_tweets, name='user_tweets'),  # Certifique-se que o nome é 'user_tweets'
    path('tweet/like/<int:tweet_id>/', like_tweet, name='like_tweet'),  # URL para curtir tweets
]
