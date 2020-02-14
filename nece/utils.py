from django.apps import apps
from django.conf import settings
from nece.models import TranslationModel


def get_translatable_models():
    for app in apps.get_app_configs():
        for model in app.get_models():
            if issubclass(model, TranslationModel):
                yield model
