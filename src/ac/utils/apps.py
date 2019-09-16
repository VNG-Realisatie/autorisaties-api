from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "ac.utils"

    def ready(self):
        from . import checks  # noqa
