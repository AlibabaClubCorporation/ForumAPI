from django.core.exceptions import ObjectDoesNotExist

from ..models import *



def get_theme_by_slug( slug : str ):
    """ Возвращает тему по полю slug """

    return Themes.objects.get( slug = slug )



def get_phor_by_theme_and_slug( slug : str, theme ):
    """ Возвращает фор по теме и слагу """

    return Phors.objects.get( slug = slug, theme = theme )



def get_user_of_client_by_pk( pk_of_user_of_client ):
    """ Возвразает пользователя клиента по первичному ключу """

    return UsersOfClient.objects.get( pk = pk_of_user_of_client )



def get_admin_status_from_user_of_client( pk_of_user_of_client ):
    """ Возвращает наличие статуса админа у пользователя клиента взятого по первичному ключу """

    return get_user_of_client_by_pk( pk_of_user_of_client ).client_admin



def get_users_of_client( pk_of_client ):
    """ Возвращает пользователей клиента по первичному ключу клиента """

    return UsersOfClient.objects.filter( client = pk_of_client )



def get_or_none( queryset, **kwargs ):
    """ Возвращает запись из queryset по ключам kwargs, если записи нет, возвращает None """
    
    try:
        return queryset.get( **kwargs )
    except ObjectDoesNotExist:
        return None