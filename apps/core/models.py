from django.conf import settings
from django.db import models
from django.utils import timezone


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Language(AbstractBaseModel):
    code = models.CharField(max_length=2, choices=settings.LANGUAGES, unique=True)
    display_name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.code
