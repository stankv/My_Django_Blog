from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    description = models.TextField(max_length=160, blank=True, verbose_name='Мета-описание', default='')
    keywords = models.CharField(max_length=60, blank=True, verbose_name='Мета-ключи', default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    description = models.TextField(max_length=160, blank=True, verbose_name='Мета-описание', default='')
    keywords = models.CharField(max_length=60, blank=True, verbose_name='Мета-ключи', default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    guide = models.BooleanField(verbose_name="Справочник", default=False)
    content = models.TextField(blank=True, verbose_name='Содержание')
    description = models.TextField(max_length=160, blank=True, verbose_name='Мета-описание', default='')
    keywords = models.CharField(max_length=160, blank=True, verbose_name='Мета-ключи', default='')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True,verbose_name='Картинка')
    count_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True,related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
