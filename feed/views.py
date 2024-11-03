from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import tweet  # Certifique-se de que este import está correto e em minúsculas

@login_required
def home(request):
    context = {'tweets': tweet.objects.all()}
    return render(request, 'feed/home.html', context)

def like_tweet(request, tweet_id):
    tweet_obj = get_object_or_404(tweet, id=tweet_id)
    if request.user in tweet_obj.likes.all():
        tweet_obj.likes.remove(request.user)  # Descurtir
        liked = False
    else:
        tweet_obj.likes.add(request.user)  # Curtir
        liked = True
    
    return JsonResponse({'liked': liked, 'total_likes': tweet_obj.total_likes()})
