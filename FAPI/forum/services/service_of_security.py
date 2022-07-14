from .service_of_data_base import get_user_of_client_by_pk

def check_UserOfClient_belongs_to_client( view ):
    """ Проверяет принадлежность пользователя клиента к клиенту """

    pk_of_user_of_client = view.kwargs.get( 'pk_of_user_of_client' )
    user_of_client = get_user_of_client_by_pk( pk_of_user_of_client )

    if user_of_client.client == view.request.user:
        return True

    return False