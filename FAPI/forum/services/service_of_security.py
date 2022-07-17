def check_UserOfClient_belongs_to_client( client, user_of_client ):
    """ Проверяет принадлежность пользователя клиента к клиенту """

    if user_of_client.client == client:
        return True

    return False