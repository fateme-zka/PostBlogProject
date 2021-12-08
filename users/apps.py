from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # the django documentation recommends doing it at this way to avoid some site attacks
    # that is how import works (that is why we are doing at this way!)
    def ready(self):
        import users.signals
