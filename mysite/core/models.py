# core/models.py

from django.db import models
from django_jalali.db import models as jmodels


class TimeStampedModel(models.Model):
    created = jmodels.jDateTimeField(auto_now_add = True)
    modified = jmodels.jDateTimeField(auto_now = True)

    class Meta:
        abstract = True
