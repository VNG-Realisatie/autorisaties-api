from django.apps import AppConfig


class ACApiConfig(AppConfig):
    name = "ac.api"

    def ready(self):
        # ensure that the metaclass for every viewset has run
        from . import viewsets  # noqa
