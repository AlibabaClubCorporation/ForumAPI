from django.urls import include, path, re_path

from . import routers
from . import views



urlpatterns = [
    path( 'api/v0.9/',  include( routers.get_router( routers.RouterOfTheme(), views.ThemeAPIViewSet, 'themes' ).urls ) ),

    path( 'api/v0.9/phors/create/', views.PhorAPIViewSet.as_view( { 'post' : 'create' } ), name = 'phor_create' ),
    path( 'api/v0.9/phors/<slug:slug_of_phor>/', views.PhorAPIViewSet.as_view( { 'get' : 'retrieve' } ), name = 'phor' ),

    path( 'api/v0.9/answers/create/', views.CreateAnswerAPIView.as_view(), name = 'answer_create' ),

    path( 'api/v0.9/auth/', include( 'djoser.urls' ) ),
	re_path( r'^api/v0.9/auth/', include( 'djoser.urls.authtoken' ) ),
]
