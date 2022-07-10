from django.contrib import admin
from django.urls import path, include

from .settings import CURRENT_API_VERSION

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/{CURRENT_API_VERSION}/', include('forum.urls')),
]
