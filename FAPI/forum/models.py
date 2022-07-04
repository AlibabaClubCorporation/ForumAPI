from django.db import models
from django.contrib.auth.models import User



class Themes(models.Model):
    """
        Класс модели темы
    """

    title = models.CharField( max_length = 256, unique = True )


class Phors(models.Model):
    """
        Класс модели фора
    """

    title = models.CharField( max_length = 256, unique = True )
    description = models.TextField( max_length = 4096, )

    date_of_creation = models.DateTimeField( auto_now_add = True, )

    theme = models.ForeignKey( Themes, on_delete = models.CASCADE, related_name = 'phors' )
    creator = models.ForeignKey( User, on_delete = models.SET_NULL, null = True, related_name = 'phors' )

    class Meta:
        ordering = [ 'date_of_creation', 'title' ]

class Answers(models.Model):
    """
        Класс модели ответа
    """

    content = models.TextField( max_length = 4096, )

    date_of_creation = models.DateTimeField( auto_now_add = True, )

    is_correct = models.BooleanField( default = False, )

    phor = models.ForeignKey( Phors, on_delete = models.CASCADE, related_name = 'answers' )
    creator = models.ForeignKey( User, on_delete = models.CASCADE, related_name = 'answers' )

    class Meta:
        ordering = [ 'date_of_creation', ]