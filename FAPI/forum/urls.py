from django.urls import path
from . import views


# Для своего удобства я не стал указывать в маршруте лишние символы наподобии: api/v1.23/
urlpatterns = [
    path( 'themes/', views.ListThemeAPIView.as_view(), name = 'themes' ),
    path( 'themes/create/', views.CreateThemeAPIView.as_view(), name = 'theme_create' ),
    path( 'themes/<slug:slug_of_theme>/', views.DetailThemeAPIView.as_view(), name = 'theme' ),

    path( 'phor/create/', views.CreatePhorAPIView.as_view(), name = 'phor_create' ),
    path( 'themes/<slug:slug_of_theme>/<slug:slug_of_phor>/', views.DetailPhorAPIView.as_view(), name = 'phor' ),

    path( 'answer/create/', views.CreateAnswerAPIView.as_view(), name = 'answer_create' ),
]
