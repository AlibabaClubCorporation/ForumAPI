from django.urls import path
from . import views


# Для своего удобства я не стал указывать в маршруте лишние символы наподобии: api/v1.23/
urlpatterns = [
    path( 'themes/', views.ListThemeAPIView.as_view() ),
    path( 'themes/create/', views.CreateThemeAPIView.as_view() ),
    path( 'themes/<slug:slug_of_theme>/', views.DetailThemeAPIView.as_view(), name = 'theme' ),

    path( 'phors/create/', views.CreatePhorAPIView.as_view() ),
    path( 'themes/<slug:slug_of_theme>/<slug:slug_of_phor>/', views.DetailPhorAPIView.as_view(), name = 'phor' ),
]
