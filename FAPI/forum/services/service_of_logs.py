from .. import models



class ObjectCreationLogs:
    """ Класс объединяющий функции, которые создают логи при создании других объектов """

    def create_client( client ):

        models.LogOfClient.objects.create( 
            client = client,
            content = f'CREATE CLIENT ( username : {client.username} | pk : {client.pk} ) ' 
        )

    def create_user_of_client( client, user_of_client ):

        models.LogOfClient.objects.create( 
            client = client,
            content = f'CLIENT ( username : {client.username} | pk : {client.pk} ) CREATED USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) '
        )
        models.LogOfUserOfClient.objects.create( 
            user_of_client = user_of_client,
            content = f'CREATE USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) ' 
        )

    def create_phor( user_of_client, phor ):

        models.LogOfUserOfClient.objects.create( 
            user_of_client = user_of_client,
            content = f'USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) CREATED PHOR ( title : {phor.title} | slug : {phor.slug} ) IN THEME ( title : {phor.theme.title} | slug : {phor.theme.slug} )' 
        )

    def create_theme( admin, theme ):

        models.LogOfClient.objects.create( 
            client = admin,
            content = f'ADMIN ( username : {admin.username} | pk : {admin.pk} ) CREATED THEME ( title : {theme.title} | slug : {theme.slug} ) '
        )
             
    def create_answer( user_of_client, answer ):

        models.LogOfUserOfClient.objects.create(
            user_of_client = user_of_client,
            content = f'USER OF CLIENT ( username : {user_of_client.username} | pk : {user_of_client.pk} ) CREATED ANSWER ( pk : {answer.pk} ) IN PHOR ( title : {answer.phor.title} | slug : {answer.phor.slug} ) '
        )



class ObjectDeletionLogs:
    """ Класс объединяющий функции, которые создают логи при удалении других объектов """

    def delete_client(  ):
        pass 

    def delete_user_of_client(  ):
        pass

    def delete_phor(  ):
        pass

    def delete_theme(  ):
        pass

    def delete_answer(  ):
        pass