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
    ]


class RouterOfPhor( routers.SimpleRouter ):
    
    routes = [
        routers.Route(
            url=r'^{prefix}/(?P<slug_of_theme>[^/.]+)/create-phor/$',
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
    ]




def get_router( router_class, viewset, prefix, basename ):
    router_class.register( prefix, viewset, basename = basename )
    return router_class