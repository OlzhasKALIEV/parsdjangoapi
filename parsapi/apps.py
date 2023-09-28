from django.apps import AppConfig
from parsapi.utils import get_json_from_api


class YourAppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parsapi'

    def ready(self):
        if not getattr(self, 'already_called', False):
            get_json_from_api()
            self.already_called = True
