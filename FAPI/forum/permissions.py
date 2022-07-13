from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny
    # Не удалять не используемые импорты. Они испольщуются в views.py

from .services.service_of_data_base import get_admin_status_from_user_of_client, get_answer_by_pk, get_or_none, get_phor_by_slug, get_user_of_client_by_pk



class IsAdminUser( BasePermission ):
    """ Класс прав доступа | Доступ разрешён, если пользователь админ API """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True 

        return False


class _IsOwnerOfPhor( BasePermission ):
    """ Класс прав доступа | Доступ разрешён, если пользователь владелец записи Phors """

    def has_object_permission(self, request, view, obj):
        pk_of_user_of_client = view.kwargs.get( 'pk_of_user_of_client' )

        if get_or_none( get_user_of_client_by_pk( pk_of_user_of_client ).phors , slug = obj.slug ):
            return True

        return False



class _IsOwnerOfAnswer( BasePermission ):
    """ Класс прав доступа | Доступ разрешён, если пользователь владелец записи Answers """

    def has_object_permission(self, request, view, obj):
        pk_of_user_of_client = view.kwargs.get( 'pk_of_user_of_client' )

        if get_or_none( get_user_of_client_by_pk( pk_of_user_of_client ).answers, pk = obj.pk ):
            return True

        return False



class IsAdminInForumOfClient( BasePermission ):
    """ Класс прав доступа | Доступ разрешён, если пользователь админ на форуме клиента """

    def has_object_permission(self, request, view, obj):
        pk_of_user_of_client = view.kwargs.get( 'pk_of_user_of_client' )
        
        return get_admin_status_from_user_of_client( pk_of_user_of_client )
    


class ObjectIsOwnedByClientOfUser( BasePermission ):
    """ Класс прав доступа | Доступ разрешён, если обьект принадлежит клиенту пользователя совершающего действие """

    def has_object_permission(self, request, view, obj):
        user_of_client = get_user_of_client_by_pk( view.kwargs.get( 'pk_of_user_of_client' ) )

        if obj.creator.client == user_of_client.client:
            return True 
        
        return False



class _StandartSpecialPermissionForModels( BasePermission ):
    """ Стандартный класс прав доступа | Доступ разрешён, если пользователь админ на форуме клиента, или админ API """

    def has_object_permission(self, request, view, obj):
        is_admin_user = IsAdminUser.has_permission( self, request, view )
        
        if ObjectIsOwnedByClientOfUser.has_object_permission( self, request, view, obj ):
            is_admin_user_in_forum_of_client = IsAdminInForumOfClient.has_object_permission( self, request, view, obj )
        else:
            is_admin_user_in_forum_of_client = False

        if is_admin_user or is_admin_user_in_forum_of_client:
            return True
        
        return False



class SpecialPermissionForPhor( _StandartSpecialPermissionForModels ):
    """ Класс прав доступа | Доступ разрешён, если пользователь админ на форуме клиента, или админ API, или враделец фора """

    def has_object_permission(self, request, view, obj):
        result_of_parent_has_object_permission = super().has_object_permission( request, view, obj )
        is_owner_of_phor = _IsOwnerOfPhor.has_object_permission( self, request, view, obj )

        if result_of_parent_has_object_permission or is_owner_of_phor:
            return True
        
        return False
    
    def has_permission(self, request, view):
        """ Наверное очень странное решение. Я не знаю как action 'change' заставить вызывать у permissions метод has_object_permission """

        obj = get_phor_by_slug( view.kwargs.get( 'slug_of_phor' ) )
        return self.has_object_permission( request, view, obj )



class SpecialPermissionForAnswer( _StandartSpecialPermissionForModels ):
    """ Класс прав доступа | Доступ разрешён, если пользователь админ на форуме клиента, или админ API, или враделец фора """

    def has_object_permission(self, request, view, obj):
        result_of_parent_has_object_permission = super().has_object_permission( request, view, obj )
        is_owner_of_answer = _IsOwnerOfAnswer.has_object_permission( self, request, view, obj )

        if result_of_parent_has_object_permission or is_owner_of_answer:
            return True

        return False
    
    def has_permission(self, request, view):
        """ Наверное очень странное решение. Я не знаю как action 'change' заставить вызывать у permissions метод has_object_permission """

        obj = get_answer_by_pk( view.kwargs.get( 'pk' ) )
        return self.has_object_permission( request, view, obj )




