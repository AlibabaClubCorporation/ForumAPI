from django.urls import include, path

from . import routers
from . import views



# Для своего удобства я не стал указывать в маршруте лишние символы наподобии: api/v1.23/
urlpatterns = [
    path( '',  include( routers.get_router( routers.RouterOfTheme(), views.ThemeAPIViewSet, 'themes' ).urls ) ),

    path( 'phors/create/', views.PhorAPIViewSet.as_view( { 'post' : 'create' } ), name = 'phor_create' ),
    path( 'phors/<slug:slug_of_phor>/', views.PhorAPIViewSet.as_view( { 'get' : 'retrieve' } ), name = 'phor' ),

    path( 'answers/create/', views.CreateAnswerAPIView.as_view(), name = 'answer_create' ),
]
