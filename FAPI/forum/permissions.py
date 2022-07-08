from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny, IsAdminUser

from .services.service_of_data_base import get_or_none



class IsOwnerOfPhor( BasePermission ):
    """ Класс прав доступа | Доступ разрешён, если пользователь владелец записи Phors """

    def has_object_permission(self, request, view, obj):
        if get_or_none( request.user.phors, { 'slug' : obj.slug } ):
            return True
        else:
            return False



class IsOwnerOfAnswer( BasePermission ):
    """ Класс прав доступа | Доступ разрешён, если пользователь владелец записи Answers """

    def has_object_permission(self, request, view, obj):
        if get_or_none( request.user.answers, pk = obj.pk ):
            return True
        else:
            return False