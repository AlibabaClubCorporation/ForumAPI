from django.core.exceptions import ObjectDoesNotExist

from ..models import *



def get_or_none( queryset = None, model = None, **kwargs ):
    """ Возвращает запись из queryset или model по ключам kwargs, если записи нет, возвращает None """
    
    assert queryset or model
    assert not(queryset and model)

    try:
        if queryset:
            return queryset.get( **kwargs )
        else:
            return model.objects.get( **kwargs )
    except ObjectDoesNotExist:
        return None

def filter_with_catching_exception( model, **kwargs ):
    try:
        return model.objects.filter( **kwargs )
    except TypeError:
        return model.objects.none()


def get_theme_by_slug( slug : str ):
    """ Возвращает тему по полю slug """

    return get_or_none( model = Themes, slug = slug )



def get_phor_by_slug( slug : str ):
    """ Возвращает фор по слагу """

    return get_or_none( model = Phors, slug = slug )



def get_answer_by_pk( pk : int ):
    """ Возвращает ответ по первичному ключу """

    return get_or_none( model = Answers, pk = pk )


def get_user_of_client_by_pk( pk ):
    """ Возвразает пользователя клиента по первичному ключу """

    return get_or_none( model = UsersOfClient, pk = pk )

# def get_user_of_client_by_pk_with_related( pk, related ):
#     """ Возвращает пользователя клиента по ключу pk и первичную модель указанную в related вмести """

#     return UsersOfClient.objects.get( pk = pk ).select_related( related )



def get_admin_status_from_user_of_client( user_of_client ):
    """ Возвращает наличие статуса админа у пользователя клиента взятого по первичному ключу """

    return user_of_client.client_admin



def get_users_of_client( pk_of_client ):
    """ Возвращает пользователей клиента по первичному ключу клиента """

    return UsersOfClient.objects.filter( client = pk_of_client )