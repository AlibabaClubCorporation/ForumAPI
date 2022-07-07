from django.urls import path
from . import views


# Для своего удобства я не стал указывать в маршруте лишние символы наподобии: api/v1.23/
urlpatterns = [
    path( 'themes/', views.ThemeAPIViewSet.as_view( { 'get' : 'list' } ), name = 'themes' ),
    path( 'themes/create/', views.ThemeAPIViewSet.as_view( { 'post' : 'create' } ), name = 'theme_create' ),
    path( 'themes/<slug:slug_of_theme>/', views.ThemeAPIViewSet.as_view( { 'get' : 'retrieve' } ), name = 'theme' ),

    path( 'phors/create/', views.PhorAPIViewSet.as_view( { 'post' : 'create' } ), name = 'phor_create' ),
    path( 'phors/<slug:slug_of_phor>/', views.PhorAPIViewSet.as_view( { 'get' : 'retrieve' } ), name = 'phor' ),

    path( 'answers/create/', views.CreateAnswerAPIView.as_view(), name = 'answer_create' ),
]
