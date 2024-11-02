from django.shortcuts import render
from .models import tweet

def home(request):
    context = {'tweets' : tweet.objects.all}
    return render(request, 'feed/home.html', context)
