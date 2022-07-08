from django.apps import AppConfig


class AccountManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account_manager'

    def ready(self) -> None:
        import account_manager.signals

        return super().ready()
