from django.db import models  
from django.urls import reverse  
from django.contrib.auth.models import User

class UserProfile(models.Model):  

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name='Возраст')  
    email = models.EmailField(max_length=254, default=None)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Author(models.Model):  
    full_name = models.CharField(max_length=100, unique=True)  
    birth_year = models.SmallIntegerField(verbose_name='Год рождения автора')  
    country = models.CharField(max_length=2, verbose_name='Страна автора')

    class Meta:
        ordering = ["full_name"] 
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})    


class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Издательство')

    class Meta:
        ordering = ["name"] 
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

    def __str__(self):
        return self.name

class Book(models.Model): 
    ISBN = models.CharField(max_length=13, blank=True)  
    title = models.CharField(max_length=100, verbose_name='Название книги')  
    description = models.TextField(blank=True, verbose_name='Описание')  
    year_release = models.SmallIntegerField(verbose_name='Год')  
    authors = models.ManyToManyField(Author, related_name='books', verbose_name='Автор')
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits = 10, decimal_places=2, default=0, verbose_name='Цена')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True, related_name='books', verbose_name='Издательство')
    country = models.CharField(max_length=2, null=True, verbose_name='Страна')
    image = models.ImageField(upload_to='img/%Y/%m/%d', blank=True, verbose_name='Обложка')

    class Meta:
        ordering = ["title"]
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

# Отображение Manytomany строки в админке      
    def display_author(self):
        return ', '.join([ author.full_name for author in self.authors.all()[:3]])
    display_author.short_description = 'Автор'

# Вывод картинок в админке
    def display_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="85"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
    display_img.short_description = 'Обложка'
    display_img.allow_tags = True


class Friend(models.Model):
    name = models.CharField(max_length=13, verbose_name='Имя')
    books = models.ManyToManyField(Book, blank=True, related_name='books', verbose_name='Выбрать книги')
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'

    def __str__(self):
        return self.name

# Отображение Manytomany строки в админке  
    def books_given(self):
        return ', '.join([ book.title for book in self.books.all()[:3]])
    books_given.short_description = 'Одолженные книги'