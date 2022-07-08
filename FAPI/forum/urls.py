from django.urls import include, path, re_path

from . import routers
from . import views



urlpatterns = [
    path( 'api/v1/',  include( routers.get_router( routers.RouterOfTheme(), views.ThemeAPIViewSet, 'themes', 'theme' ).urls ) ),

    path( 'api/v1/', include( routers.get_router( routers.RouterOfPhor(), views.PhorAPIViewSet, 'themes', 'theme' ).urls ) ),

    path( 'api/v1/', include( routers.get_router( routers.RouterOfAnswer(), views.AnswerAPIViewSet, 'themes', 'theme' ).urls ) ),
    # path( 'api/v1/themes/<slug:slug_of_theme>/<slug:slug_of_phor>/create-answer/', views.CreateAnswerAPIView.as_view(), name = 'answer-create' ),

    path( 'api/v1/auth/', include( 'djoser.urls' ) ),
	re_path( r'^api/v1/auth/', include( 'djoser.urls.authtoken' ) ),
]
