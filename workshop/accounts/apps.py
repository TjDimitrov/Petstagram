from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'workshop.accounts'

    def ready(self):
        import workshop.accounts.signals
        result = super().ready()
        return result
