from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here.

def index(request):
    # print(dir(request))
    news = [x for x in News.objects.all() if x.is_published]
    context = {
        'news': news,
        'title': 'Список новостей'

    }
    return render(request, template_name='news/index.html', context=context)
