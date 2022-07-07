from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import permissions

from .serializers import CreateAnswerSerializer, CreatePhorSerializer, ThemeSerializer, ListThemeSerializer, PhorSerializer, CreateThemeSerializer
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

class CreateThemeAPIView( CreateAPIView ):
    """ Класс представления, для создания темы """

    serializer_class = CreateThemeSerializer
    permission_classes = ( permissions.IsAuthenticated, )



class DetailPhorAPIView( RetrieveAPIView ):
    """ Класс представления, для отображения подробной информации фора """

    queryset = Phors.objects.all()
    serializer_class = PhorSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug_of_phor'

class CreatePhorAPIView( CreateAPIView ):
    """ Класс представления, для создания форов """

    serializer_class = CreatePhorSerializer
    permission_classes = ( permissions.IsAuthenticated, )



class CreateAnswerAPIView( CreateAPIView ):
    """ Класс представления, для создания ответов """

    serializer_class = CreateAnswerSerializer
    permission_classes = ( permissions.IsAuthenticated, )


    