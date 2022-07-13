from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .serializers import *
from .models import *
from . import permissions

from .services.service_of_data_base import *
from .services.service_of_logs import ObjectDeletionLogs



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
        
        return ( permissions.IsAdminUser(), )
    

    def destroy(self, request, *args, **kwargs):
        theme = get_theme_by_slug( kwargs.get( 'slug_of_theme' ) )
        admin = request.user

        ObjectDeletionLogs.delete_theme( admin = admin, theme = theme )

        return super().destroy(request, *args, **kwargs)



class PhorAPIViewSet( viewsets.ModelViewSet ):
    """ Набор представлений, для модели Phors """

    lookup_field = 'slug'
    lookup_url_kwarg = 'slug_of_phor'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PhorSerializer
        elif self.action == 'create':
            return CreatePhorSerializer
        
        return ChangeDescriptionOfPhorSerializer
    
    def get_permissions(self):
        if self.action == 'retrieve':
            return ( permissions.AllowAny(), )
        elif self.action in ( 'destroy', 'change' ):
            return ( permissions.SpecialPermissionForPhor(), )
        
        return ( permissions.IsAuthenticated(), )
    
    def get_queryset(self):
        if self.action == 'retrieve':
            slug_of_phor = self.kwargs.get( 'slug_of_phor' )
            slug_of_theme = self.kwargs.get( 'slug_of_theme' )

            return Phors.objects.filter( slug = slug_of_phor, theme__slug = slug_of_theme )
        
        return Phors.objects.all()
    

    def destroy(self, request, *args, **kwargs):
        phor = get_phor_by_slug( kwargs.get( 'slug_of_phor' ) )
        user_of_client = get_user_of_client_by_pk( kwargs.get( 'pk_of_user_of_client' ) )

        ObjectDeletionLogs.delete_phor( user_of_client = user_of_client, phor = phor )

        return super().destroy(request, *args, **kwargs)
    

    def change( self, request, slug_of_theme = None, slug_of_phor = None, pk_of_user_of_client = None ):
        serializer = ChangeDescriptionOfPhorSerializer( data = request.data )

        if serializer.is_valid():
            serializer.save( slug_of_phor = slug_of_phor )

            return Response( status = 200 )
        else:
            return Response( status = 400 )





class AnswerAPIViewSet( viewsets.ModelViewSet ):
    """ Набор представлений, для модели Answers """

    queryset = Answers.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return ( permissions.IsAuthenticated(), )
        
        return ( permissions.SpecialPermissionForAnswer(), )
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateAnswerSerializer
        
        return ChangeContentOfAnswerSerializer
    
    def destroy(self, request, *args, **kwargs):
        answer = get_answer_by_pk( kwargs.get( 'pk' ) )
        user_of_client = get_user_of_client_by_pk( kwargs.get( 'pk_of_user_of_client' ) )

        ObjectDeletionLogs.delete_answer( user_of_client = user_of_client, answer = answer )

        return super().destroy(request, *args, **kwargs)
    
    def change( self, request, slug_of_theme = None, slug_of_phor = None, pk_of_user_of_client = None, pk = None ):
        serializer = ChangeContentOfAnswerSerializer( data = request.data )

        if serializer.is_valid():
            serializer.save( pk_of_answer = pk )

            return Response( status = 200 )
        else:
            return Response( status = 400 )



class UserOfClientAPIViewSet( viewsets.ModelViewSet ):
    """ Набор представлений, для модели UserOfClient """

    queryset = UsersOfClient.objects.all()
    permission_classes = ( permissions.IsAuthenticated, )

    lookup_url_kwarg = 'pk_of_user_of_client'

    def get_serializer_class(self):
        if self.action in ( 'list', 'retrieve' ):
            return UserOfClientSerializer

        return CreateUserOfClientSerializer
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return UsersOfClient.objects.all()
        
        return get_users_of_client( self.request.user.pk )


    def destroy(self, request, *args, **kwargs):
        user_of_client = get_user_of_client_by_pk( kwargs.get( 'pk_of_user_of_client' ) )
        client = request.user

        ObjectDeletionLogs.delete_user_of_client( client = client, user_of_client = user_of_client )

        return super().destroy(request, *args, **kwargs)



class LogOfClientAPIView( ListAPIView ):
    """ Класс представления для модели LogOfClient """

    serializer_class = LogOfClientSerializer

    def get_queryset(self):
        client = self.request.user

        if client.is_superuser:
            return LogOfClient.objects.all()
        else:
            return LogOfClient.objects.filter( client = client )


class LogOfUserOfClientAPIView( ListAPIView ):
    """ Класс представления для модели LogOfUserOfClient """

    serializer_class = LogOfUserOfClientSerializer

    def get_queryset(self):
        client = self.request.user
        user_of_client =  get_user_of_client_by_pk( self.kwargs.get( 'pk_of_user_of_client' ) )

        if client.is_superuser:
            return LogOfUserOfClient.objects.filter( user_of_client = user_of_client )
        else:
            return LogOfUserOfClient.objects.filter( user_of_client = user_of_client, user_of_client__client = client )