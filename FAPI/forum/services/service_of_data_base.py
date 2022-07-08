from django.core.exceptions import ObjectDoesNotExist

from ..models import *



def get_theme_by_slug( slug : str ):
    """ Возвращает тему по полю slug """

    return Themes.objects.get( slug = slug )


def get_phor_by_theme_and_slug( slug : str, theme ):
    """ Возвращает фор по теме и слагу """

    return Phors.objects.get( slug = slug, theme = theme )



def get_or_none( queryset, **kwargs ):
    """ Возвращает запись из queryset по ключам kwargs, если записи нет, возвращает None """
    
    try:
        return queryset.get( **kwargs )
    except ObjectDoesNotExist:
        return None