from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Themes(models.Model):
    """
        Класс модели темы
    """

    title = models.CharField( max_length = 128, unique = True, )

    slug = models.SlugField( max_length = 256, unique = True, db_index = True, )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse( 'theme', kwargs = { 'theme_slug' : self.slug } )


class Phors(models.Model):
    """
        Класс модели фора
    """

    title = models.CharField( max_length = 128, unique = True )
    description = models.TextField( max_length = 4096, )

    date_of_creation = models.DateTimeField( auto_now_add = True, )

    theme = models.ForeignKey( Themes, on_delete = models.CASCADE, related_name = 'phors' )
    creator = models.ForeignKey( User, on_delete = models.SET_NULL, null = True, related_name = 'phors' )

    slug = models.SlugField( max_length = 256, unique = True, db_index = True, )

    class Meta:
        ordering = [ 'date_of_creation', 'title' ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse( 'phor', kwargs = { 'phor_slug' : self.slug } )

class Answers(models.Model):
    """
        Класс модели ответа
    """

    content = models.TextField( max_length = 4096, )

    date_of_creation = models.DateTimeField( auto_now_add = True, )

    is_correct = models.BooleanField( default = False, )

    phor = models.ForeignKey( Phors, on_delete = models.CASCADE, related_name = 'answers' )
    creator = models.ForeignKey( User, on_delete = models.CASCADE, related_name = 'answers' )
    parent_answer = models.ForeignKey( 'self', on_delete = models.CASCADE, blank = True, null = True, related_name = 'child_answers' )

    class Meta:
        ordering = [ 'date_of_creation', ]