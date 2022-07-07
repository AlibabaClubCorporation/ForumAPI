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
    queryset = Phors.objects.all()
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



class CreateAnswerAPIView( CreateAPIView ):
    """ Класс представления, для создания ответов """

    serializer_class = CreateAnswerSerializer
    permission_classes = ( permissions.IsAuthenticated, )


    