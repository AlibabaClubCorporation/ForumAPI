from django.http import JsonResponse
from ..models import *



def get_theme_by_slug( slug : str ) -> models.Model:
    """ Возвращает тему по полю slug """

    return Themes.objects.get( slug = slug )


def get_phor_by_theme_and_slug( slug, theme ):
    """ Возвращает фор по теме и слагу """

    return Phors.objects.get( slug = slug, theme = theme )