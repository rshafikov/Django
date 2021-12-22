import django.db.models
from django.db import models


# id - INT
# title - Varchar
# content - text
# created_at - DateTime
# updated_at - DateTime
# photo - Image
# is_published - Boolean

class News(models.Model):
    # ID по умолчанию. Создание модели нашей БД)
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержание')  # Blank - необязательное поле для заполнения можно не заполнять
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')  # только изображение
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)  # PROTECT обеспечивает защиту от удаления

    def __str__(self):
        return self.title

    # открыть консоль DJANGO IntercativeConsole - python3 manage.py shell не забывать импортировать модель из from
    # news.models import News >>> from django.db import connection >>> connection.queries [{'sql': 'INSERT INTO
    # "news_news" ("title", "content", "created_at", "updated_at", "photo", "is_published") SELECT \'Новость 1\',
    # \'Контент новости 1\', \'2021-12-17 11:49:06.376524\', \'2021-12-17 11:49:06.377051\', \'\', 1 RETURNING
    # "news_news"."id"', 'time': '0.002'}]
    # >>> news4 = News.objects.create(title='news 4', content='content news 4')

    # Настройка админки - отображение разлчных полей
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']  # влияет на views приложения


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категория', db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']  # влияет на views приложения
