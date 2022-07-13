from django.urls import include, path, re_path

from . import routers
from . import views



urlpatterns = [
    path( '',  include( routers.get_router( routers.RouterOfTheme(), views.ThemeAPIViewSet, 'themes', 'theme' ).urls ) ),

    path( '', include( routers.get_router( routers.RouterOfPhor(), views.PhorAPIViewSet, 'themes', 'phor' ).urls ) ),

    path( '', include( routers.get_router( routers.RouterOfAnswer(), views.AnswerAPIViewSet, 'themes', 'answer' ).urls ) ),

    path( '', include( routers.get_router( routers.RouterOfUserOfClient(), views.UserOfClientAPIViewSet, 'client-users', 'user-of-client' ).urls ) ),

    path( 'logs_of_client/', views.LogOfClientAPIView.as_view() , name = 'logs_of_client' ),

    path( 'auth/', include( 'djoser.urls' ) ),
	re_path( r'^auth/', include( 'djoser.urls.authtoken' ) ),
]
