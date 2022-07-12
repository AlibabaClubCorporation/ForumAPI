from django.db import models
from django.urls import reverse



class Log( models.Model ):
    """
        Класс абстрактной модели лога ( Записи событий )
    """

    content = models.CharField( verbose_name = 'Содержимое лога', max_length = 512, )
    date_of_creation = models.DateTimeField( verbose_name = 'Время создания лога', auto_now_add = True,  )

    class Meta:
        abstract = True
    
    def get_absolute_url( self ):
        return reverse( 'logs', kwargs = { 'pk_of_log' : self.pk } )