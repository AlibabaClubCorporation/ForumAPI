from django.db import models
from django.contrib.auth.models import User



class Status( models.Model ):
    """
        Модель статуса пользователя
    """

    is_forum = models.BooleanField( verbose_name = 'Наличие статуса форума' )
    user = models.OneToOneField( verbose_name = 'Пользователь', to = User, on_delete = models.CASCADE, related_name = 'status', )

    def __str__(self):
        return f' Status of {self.user.username} '

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'