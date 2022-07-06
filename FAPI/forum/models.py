from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Themes(models.Model):
    """
        Класс модели темы
    """

    title = models.CharField( verbose_name = "Название темы", max_length = 128, unique = True, )

    slug = models.SlugField( verbose_name = "Слаг темы", max_length = 256, unique = True, db_index = True, )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse( 'theme', kwargs = { 'slug_of_theme' : self.slug } )

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Phors(models.Model):
    """
        Класс модели фора
    """

    title = models.CharField( verbose_name = "Заголовок фора", max_length = 128, unique = True )
    description = models.TextField( verbose_name = "Описание проблемы в форе", max_length = 4096, )

    date_of_creation = models.DateTimeField( verbose_name = "Дата создания фора", auto_now_add = True, )

    theme = models.ForeignKey( verbose_name = "Ссылка на тему фора", to = Themes, on_delete = models.CASCADE, related_name = 'phors' )
    creator = models.ForeignKey( verbose_name = "Ссылка на создателя фора", to = User, on_delete = models.SET_NULL, null = True, related_name = 'phors' )

    slug = models.SlugField( verbose_name = "Слаг фора", max_length = 256, unique = True, db_index = True, )

    class Meta:
        ordering = [ 'date_of_creation', 'title' ]
        verbose_name = 'Фор'
        verbose_name_plural = 'Форы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse( 'phor', kwargs = { 'slug_of_phor' : self.slug, 'slug_of_theme' : self.theme.slug } )

class Answers(models.Model):
    """
        Класс модели ответа
    """

    content = models.TextField( verbose_name = "Содержимое ответа", max_length = 4096, )

    date_of_creation = models.DateTimeField( verbose_name = "Дата создания ответа", auto_now_add = True, )

    is_correct = models.BooleanField( verbose_name = "Наличие статуса 'правильный ответ' у ответа", default = False, )

    phor = models.ForeignKey( verbose_name = "Ссылка на фор ответа", to = Phors, on_delete = models.CASCADE, related_name = 'answers' )
    creator = models.ForeignKey( verbose_name = "Ссылка на создателя ответа", to = User, on_delete = models.CASCADE, related_name = 'answers' )
    parent_answer = models.ForeignKey( verbose_name = "Ссылка на родительский ответ ответа", to = 'self', on_delete = models.CASCADE, blank = True, null = True, related_name = 'child_answers' )

    class Meta:
        ordering = [ 'date_of_creation', ]
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'