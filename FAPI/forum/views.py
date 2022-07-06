from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import ThemeSerializer, ListThemeSerializer, PhorSerializer
from .models import Themes, Phors



class ListThemeAPIView( ListAPIView ):
    """ Класс представления, для отображения списка тем """

    queryset = Themes.objects.all()
    serializer_class = ListThemeSerializer

class DetailThemeAPIView( RetrieveAPIView ):
    """ Класс представления, для отображения подробной информации темы """

    queryset = Themes.objects.all()
    serializer_class = ThemeSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug_of_theme'



class DetailPhorAPIView( RetrieveAPIView ):
    """ Класс представления, для отображения подробной информации фора """

    queryset = Phors.objects.all()
    serializer_class = PhorSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug_of_phor'