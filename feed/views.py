from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import tweet  # Importação do modelo de tweet em minúsculas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django import forms

# Formulário para criar um tweet
class TweetForm(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['text']

class TweetListView(LoginRequiredMixin, ListView):
    model = tweet
    template_name = 'feed/home.html'
    ordering = ['-datetime']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TweetForm()  # Adicionando o formulário ao contexto
        return context

    def post(self, request, *args, **kwargs):
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet_instance = form.save(commit=False)
            tweet_instance.uname = request.user  # Atribuindo o usuário ao tweet
            tweet_instance.save()  # Salva o tweet no banco de dados
            return redirect('home')  # Redireciona para a página inicial após criar o tweet
        return self.get(request, *args, **kwargs)  # Retorna a mesma página se o formulário não for válido

from django.http import JsonResponse

@login_required
def edit_tweet(request, tweet_id):
    tweet_instance = get_object_or_404(tweet, id=tweet_id, uname=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, instance=tweet_instance)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
def delete_tweet(request, tweet_id):
    tweet_instance = get_object_or_404(tweet, id=tweet_id, uname=request.user)
    if request.method == 'POST':
        tweet_instance.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def user_tweets(request):
    # Exibe apenas os tweets do usuário autenticado
    context = {'tweets': tweet.objects.filter(uname=request.user)}
    return render(request, 'feed/user_tweets.html', context)

def like_tweet(request, tweet_id):
    tweet_obj = get_object_or_404(tweet, id=tweet_id)
    if request.user in tweet_obj.likes.all():
        tweet_obj.likes.remove(request.user)  # Descurtir
        liked = False
    else:
        tweet_obj.likes.add(request.user)  # Curtir
        liked = True
    return JsonResponse({'liked': liked, 'total_likes': tweet_obj.total_likes()})
