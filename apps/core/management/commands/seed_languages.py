from django.core.management.base import BaseCommand
from apps.core.models import Language
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        d = [Language(code=l[0], display_name=l[1]) for l in settings.LANGUAGES]
        Language.objects.bulk_create(d)
