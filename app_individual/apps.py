from django.apps import AppConfig


class AppIndividualConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_individual'
    verbose_name = 'Индивидуальные предприниматели'
