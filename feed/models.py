from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class tweet(models.Model):
    text = models.CharField(max_length=280, default='')
    datetime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='tweet_likes', blank=True)

    def total_likes(self):
        return self.likes.count()
