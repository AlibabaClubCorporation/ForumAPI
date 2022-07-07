from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import CreateAnswerSerializer, CreatePhorSerializer, ThemeSerializer, ListThemeSerializer, PhorSerializer, CreateThemeSerializer
from .models import Themes, Phors
from .paginations import ListPagination



class ThemeAPIViewSet( viewsets.ModelViewSet ):
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



class CreateAnswerAPIView( CreateAPIView ):
    """ Класс представления, для создания ответов """

    serializer_class = CreateAnswerSerializer
    permission_classes = ( permissions.IsAuthenticated, )


    