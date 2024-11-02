from django.shortcuts import render

tweets = [{'name': 'Nandinha', 'text': 'My first tweet'},{'name': 'Gabs', 'text' : 'This is my second tweet'}]


def home(request):
    context = {'tweets' : tweets}
    return render(request, 'feed/home.html', context)
