from django.urls import path
from . import views

urlpatterns = [
    path( '', views.PhorAPIView.as_view() )
]
