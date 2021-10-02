from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self) -> None:
        # importing to use signals so profiles are created 
        # when users are created
        import users.signals

        return super().ready()
