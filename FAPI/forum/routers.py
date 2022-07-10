from rest_framework import routers



class RouterOfTheme(routers.SimpleRouter): 
    
    routes = [
        routers.Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),

        routers.Route(
            url=r'^{prefix}/create-theme/$',
            mapping={'post': 'create'},
            name='{basename}-create',
            detail=True,
            initkwargs={'suffix': 'Create'}
        ),

        routers.Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),

        routers.Route(
            url=r'^{prefix}/{lookup}/delete-theme/$',
            mapping={'delete': 'destroy'},
            name='{basename}-delete',
            detail=True,
            initkwargs={'suffix': 'Delete'}
        ),
    ]


class RouterOfPhor( routers.SimpleRouter ):
    
    routes = [
        routers.Route(
            url=r'^{prefix}/(?P<slug_of_theme>[^/.]+)/(?P<pk_of_user_of_client>[^/.]+)/create-phor/$',
            mapping={'post': 'create'},
            name='{basename}-create',
            detail=True,
            initkwargs={'suffix': 'Create'}
        ),

        routers.Route(
            url=r'^{prefix}/(?P<slug_of_theme>[^/.]+)/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),

        routers.Route(
            url=r'^{prefix}/(?P<slug_of_theme>[^/.]+)/{lookup}/(?P<pk_of_user_of_client>[^/.]+)/delete-phor/$',
            mapping={'delete': 'destroy'},
            name='{basename}-delete',
            detail=True,
            initkwargs={'suffix': 'Delete'}
        ),
    ]


class RouterOfAnswer( routers.SimpleRouter ):

    routes = [
        routers.Route(
            url=r'^{prefix}/(?P<slug_of_theme>[^/.]+)/(?P<slug_of_phor>[^/.]+)/(?P<pk_of_user_of_client>[^/.]+)/create-answer$',
            mapping={'post': 'create'},
            name='{basename}-create',
            detail=True,
            initkwargs={'suffix': 'Create'}
        ),

        routers.Route(
            url=r'^{prefix}/(?P<slug_of_theme>[^/.]+)/(?P<slug_of_phor>[^/.]+)/{lookup}/(?P<pk_of_user_of_client>[^/.]+)/delete-answer/$',
            mapping={'delete': 'destroy'},
            name='{basename}-delete',
            detail=True,
            initkwargs={'suffix': 'Delete'}
        ),
    ]



class RouterOfUserOfClient( routers.SimpleRouter ):

    routes = [
        routers.Route(
            url=r'^{prefix}/create-user-of-client/$',
            mapping={'post': 'create'},
            name='{basename}-create',
            detail=True,
            initkwargs={'suffix': 'Create'}
        ),

        routers.Route(
            url=r'^{prefix}/{lookup}/delete-user-of-client/$',
            mapping={'delete': 'destroy'},
            name='{basename}-delete',
            detail=True,
            initkwargs={'suffix': 'Delete'}
        ),

        routers.Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=True,
            initkwargs={'suffix': 'List'}
        ),

        routers.Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='{basename}-retrieve',
            detail=True,
            initkwargs={'suffix': 'Retrieve'}
        ),
    ]



def get_router( router_class, viewset, prefix, basename ):
    router_class.register( prefix, viewset, basename = basename )
    return router_class