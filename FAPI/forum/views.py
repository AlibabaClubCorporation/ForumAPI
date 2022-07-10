from rest_framework import viewsets

from .serializers import CreateAnswerSerializer, CreatePhorSerializer, CreateUserOfForumSerializer, ThemeSerializer, ListThemeSerializer, PhorSerializer, CreateThemeSerializer, UserOfForumSerializer
from .models import *
from . import permissions

from .services.service_of_data_base import get_users_of_client



class ThemeAPIViewSet( viewsets.ModelViewSet ):
    """ Набор представлений, для модели Themes """

    queryset = Themes.objects.all()
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
            return ( permissions.IsAdminUser(), )



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
        elif self.action == 'destroy':
            return ( permissions.PermissionForDeletePhor(), )
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

    def get_permissions(self):
        if self.action == 'create':
            return ( permissions.IsAuthenticated(), )
        else:
            return ( permissions.PermissionForDeleteAnswer(), )



class UserOfClientAPIViewSet( viewsets.ModelViewSet ):
    """ Набор представлений, для модели UserOfClient """

    queryset = UsersOfClient.objects.all()
    permission_classes = ( permissions.IsAuthenticated, )

    lookup_url_kwarg = 'pk_of_user_of_client'

    def get_serializer_class(self):
        if self.action in ( 'list', 'retrieve' ):
            return UserOfForumSerializer
        else:
            return CreateUserOfForumSerializer
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return UsersOfClient.objects.all()
        else:
            return get_users_of_client( self.request.user.pk )