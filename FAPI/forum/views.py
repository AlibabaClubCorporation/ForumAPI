from rest_framework import viewsets
from rest_framework import permissions

from .serializers import CreateAnswerSerializer, CreatePhorSerializer, ThemeSerializer, ListThemeSerializer, PhorSerializer, CreateThemeSerializer
from .models import *
from .paginations import ListPagination



class ThemeAPIViewSet( viewsets.ModelViewSet ):
    """ Набор представлений, для модели Themes """

    queryset = Themes.objects.all()
    pagination_class = ListPagination
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug_of_theme'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ThemeSerializer
        elif self.action == 'list':
            return ListThemeSerializer
        elif self.action == 'create':
            return CreateThemeSerializer
    
    def get_permissions(self):
        if self.action in ( 'retrieve', 'list' ):
            return ( permissions.AllowAny(), )
        else:
           return ( permissions.IsAuthenticated(), )


class PhorAPIViewSet( viewsets.ModelViewSet ):
    """ Набор представлений, для модели Phors """

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug_of_phor'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PhorSerializer
        elif self.action == 'create':
            return CreatePhorSerializer
    
    def get_permissions(self):
        if self.action == 'retrieve':
            return ( permissions.AllowAny(), )
        else:
            return ( permissions.IsAuthenticated(), )
    
    def get_queryset(self):
        if self.action == 'retrieve':
            slug_of_phor = self.kwargs.get( 'slug_of_phor' )
            slug_of_theme = self.kwargs.get( 'slug_of_theme' )

            return Phors.objects.filter( slug = slug_of_phor, theme__slug = slug_of_theme )
        else:
            return Phors.objects.all()


class AnswerAPIViewSet( viewsets.ModelViewSet ):
    """ Набор представлений, для модели Answers """

    queryset = Answers.objects.all()
    serializer_class = CreateAnswerSerializer
    permission_classes = ( permissions.IsAuthenticated, )
