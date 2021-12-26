from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here.

def index(request):
    # print(dir(request))
    news = [x for x in News.objects.all() if x.is_published]
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)


def registration(request):
    return render(request, template_name='news/registration.html')


def registration_complete(request):
    print(request.POST)
    return HttpResponse('Вы зарегистрированы!')


def new_post(request):
    if request.method == 'POST':
        new_news = News.objects.create(title=request.POST['title'], content=request.POST['text'])
        new_news.save()
    return render(request, template_name='news/new_post.html')


def draw(request):
    return render(request, template_name='news/draw.html')
