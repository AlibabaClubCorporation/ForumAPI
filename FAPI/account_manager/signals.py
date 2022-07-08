from django.db.models import signals
from django.dispatch import receiver

from .models import User, Status



@receiver( signals.post_save, sender = User )
def assignen_status_to_user( sender, instance, **kwargs ):
    """ После инициализации нового пользователя, соединяет его с моделью Status """

    Status.objects.create( is_forum = False, user = instance )