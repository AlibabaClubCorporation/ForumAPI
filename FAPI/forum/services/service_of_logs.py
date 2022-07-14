from .. import models



class ObjectCreationLogs:
    """ Класс объединяющий функции, которые создают логи при создании других объектов """

    def create_client( client ):
        """ Добавляет лог события 'Создание клиента' """

        models.LogOfClient.objects.create( 
            client = client,
            content = f'CREATE CLIENT ( username : {client.username} | pk : {client.pk} ) ' 
        )

    def create_user_of_client( client, user_of_client ):
        """ Добавляет логи события 'Создание пользователя клиента' """

        models.LogOfClient.objects.create( 
            client = client,
            content = f'CLIENT ( username : {client.username} | pk : {client.pk} ) CREATED USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) '
        )
        models.LogOfUserOfClient.objects.create( 
            user_of_client = user_of_client,
            content = f'CREATE USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) ' 
        )

    def create_phor( user_of_client, phor ):
        """ Добавляет лог события 'Создание фора' """

        models.LogOfUserOfClient.objects.create( 
            user_of_client = user_of_client,
            content = f'USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) CREATED PHOR ( title : {phor.title} | slug : {phor.slug} ) IN THEME ( title : {phor.theme.title} | slug : {phor.theme.slug} )' 
        )

    def create_theme( admin, theme ):
        """ Добавляет лог события 'Создание темы' """

        models.LogOfClient.objects.create( 
            client = admin,
            content = f'ADMIN ( username : {admin.username} | pk : {admin.pk} ) CREATED THEME ( title : {theme.title} | slug : {theme.slug} ) '
        )
             
    def create_answer( user_of_client, answer ):
        """ Добавляет лог события 'Создание ответа' """

        models.LogOfUserOfClient.objects.create(
            user_of_client = user_of_client,
            content = f'USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) CREATED ANSWER ( pk : {answer.pk} ) IN PHOR ( title : {answer.phor.title} | slug : {answer.phor.slug} ) '
        )



class ObjectDeletionLogs:
    """ Класс объединяющий функции, которые создают логи при удалении других объектов """

    def delete_user_of_client( client, user_of_client ):
        """ Добавляет логи события 'Удаление пользователя клиента' """

        models.LogOfClient.objects.create( 
            client = client,
            content = f'CLIENT ( username : {client.username} | pk : {client.pk} ) DELETED USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) '
        )

    def delete_phor( user_of_client, phor ):
        """ Добавляет лог события 'Удаление фора' """

        models.LogOfUserOfClient.objects.create( 
            user_of_client = user_of_client,
            content = f'USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) DELETED PHOR ( title : {phor.title} | slug : {phor.slug} ) IN THEME ( title : {phor.theme.title} | slug : {phor.theme.slug} )' 
        )

    def delete_theme( admin, theme ):
        """ Добавляет лог события 'Удаление темы' """

        models.LogOfClient.objects.create( 
            client = admin,
            content = f'ADMIN ( username : {admin.username} | pk : {admin.pk} ) DELETED THEME ( title : {theme.title} | slug : {theme.slug} ) '
        )
             
    def delete_answer( user_of_client, answer ):
        """ Добавляет лог события 'Удаление ответа' """

        models.LogOfUserOfClient.objects.create(
            user_of_client = user_of_client,
            content = f'USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) DELETED ANSWER ( pk : {answer.pk} ) IN PHOR ( title : {answer.phor.title} | slug : {answer.phor.slug} ) '
        )



class ObjectChangingLogs:
    """ Класс объединяющий функции, которые создают логи при удалении других объектов """

    def change_phor( user_of_client, phor, before ):
        """ Добавляет лог события 'Изменение содержимого фора' """

        models.LogOfUserOfClient.objects.create( 
            user_of_client = user_of_client,
            content = f'USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) CHANGE PHOR ( title : {phor.title} | slug : {phor.slug} )  |  BEFORE ( description : {before} ) CURRENT ( description : { phor.description } )'
        )

    def change_answer( user_of_client, answer, before ):
        """ Добавляет лог события 'Изменение содержимого ответа' """

        models.LogOfUserOfClient.objects.create( 
            user_of_client = user_of_client,
            content = f'USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) CHANGE AMSWER ( pk : { answer.pk } ) IN PHOR ( title : {answer.phor.title} | slug : {answer.phor.slug} ) |  BEFORE ( content : {before} ) CURRENT ( content : { answer.content } )'
        )
