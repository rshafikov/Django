import django.db.models
from django.db import models


# Create your models here.

# id - INT
# title - Varchar
# content - text
# created_at - DateTime
# updated_at - DateTime
# photo - Image
# is_published - Boolean


class News(models.Model):
    # ID по умолчанию. Создание модели нашей БД)
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)  # Blank - необязательное поле для заполнения можно не заполнять
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # только изображение
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# открыть консоль DJANGO IntercativeConsole - python3 manage.py shell
# не забывать импортировать модель из from news.models import News
# >>> from django.db import connection
# >>> connection.queries
# [{'sql': 'INSERT INTO "news_news" ("title", "content", "created_at", "updated_at", "photo", "is_published") SELECT \'Новость 1\', \'Контент новости 1\', \'2021-12-17 11:49:06.376524\', \'2021-12-17 11:49:06.377051\', \'\', 1 RETURNING "news_news"."id"', 'time': '0.002'}]

# >>> news4 = News.objects.create(title='news 4', content='content news 4')

