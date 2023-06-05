from oscar.apps.checkout.models import *  # noqa isort:skip
from django.db import models
from oscar.apps.partner.abstract_models import AbstractPartner


class Partner(AbstractPartner):
    Company = models.CharField(max_length=300, blank=True)
