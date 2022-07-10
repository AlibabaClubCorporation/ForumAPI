from django.urls import include, path, re_path

from . import routers
from . import views



urlpatterns = [
    path( '',  include( routers.get_router( routers.RouterOfTheme(), views.ThemeAPIViewSet, 'themes', 'theme' ).urls ) ),

    path( '', include( routers.get_router( routers.RouterOfPhor(), views.PhorAPIViewSet, 'themes', 'theme' ).urls ) ),

    path( '', include( routers.get_router( routers.RouterOfAnswer(), views.AnswerAPIViewSet, 'themes', 'theme' ).urls ) ),

    path( 'auth/', include( 'djoser.urls' ) ),
	re_path( r'^auth/', include( 'djoser.urls.authtoken' ) ),
]
