from rest_framework.generics import ListAPIView

from .serializers import ThemeSerializer
from .models import Themes


class PhorAPIView( ListAPIView ):
    queryset = Themes.objects.filter( pk = 1 )
    serializer_class = ThemeSerializer
