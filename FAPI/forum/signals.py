from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .services.service_of_logs import *



@receiver( post_save, sender = models.UsersOfClient )
def signal_of_created_user_of_client( sender, instance, **kwargs ):
    """ Сигнал срабатывающий при создании пользователя клиента """

    ObjectCreationLogs.create_user_of_client( user_of_client = instance, client = instance.client )

@receiver( post_save, sender = models.User )
def signal_of_created_client( sender, instance, **kwargs ):
    """ Сигнал срабатывающий при создании клиента """

    ObjectCreationLogs.create_client( client = instance )

@receiver( post_save, sender = models.Themes )
def signal_of_created_theme( sender, instance, **kwargs ):
    """ Сигнал срабатывающий при создании темы """

    ObjectCreationLogs.create_theme( admin = instance.creator, theme = instance )

@receiver( post_save, sender = models.Phors )
def signal_of_created_phor( sender, instance, **kwargs ):
    """ Сигнал срабатывающий при создании фора """

    ObjectCreationLogs.create_phor( user_of_client = instance.creator, phor = instance )

@receiver( post_save, sender = models.Answers )
def signal_of_created_answer( sender, instance, **kwargs ):
    """ Сигнал срабатывающий при создании ответа """

    ObjectCreationLogs.create_answer( user_of_client = instance.creator, answer = instance )