from django.urls import path
from . import views

urlpatterns = [
    path( 'themes/', views.ListThemeAPIView.as_view() ),
    path( 'themes/<slug:slug_of_theme>', views.DetailThemeAPIView.as_view() ),

    path( 'themes/<slug:slug_of_theme>/<slug:slug_of_phor>', views.DetailPhorAPIView.as_view() ),
]
