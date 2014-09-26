import datetime
from django.db import models
from model_utils.models import TimeStampedModel
from model_utils import Choices
from django.conf import settings
from location.models import Address


class ContractType(TimeStampedModel):
    TYPE = Choices(
        ('res30', _('New')),
        ('under_review', _('Under Review')),
        ('approved', _('Approved')),
        ('declined', _('Declined')),
        ('deducting', _('Deducting')),
        ('complete', _('Complete'))
    )

class Customer(TimeStampedModel):
    acct_num = models.IntegerField(verbose_name = _("Account Number"))
    acct_key = models.CharField(max_length=20, verbose_name = _("Access Key"))
    acct_name = models.CharField(max_length=50, verbose_name = _("Account Name"))
    first_name1 = models.CharField(max_length=50, verbose_name = _("First Name 1"))
    last_name1 = models.CharField(max_length=50, verbose_name = _("Last Name 1"))
    first_name2 = models.CharField(max_length=50, verbose_name = _("First Name 2"))
    last_name2 = models.CharField(max_length=50, verbose_name = _("Last Name 2"))
    phone1_name = models.CharField(max_length=100, null=True, blank=True, verbose_name = _("Phone 1 Name"))
    phone1_number = models.CharField(max_length=15, null=True, blank=True, verbose_name = _("Phone 1 Number"))
    phone1_mobile = models.BooleanField(default=False, verbose_name=_("Phone 1 Is Mobile"))
    phone2_name = models.CharField(max_length=100, null=True, blank=True, verbose_name = _("Phone 2 Name"))
    phone2_number = models.CharField(max_length=15, null=True, blank=True, verbose_name = _("Phone 2 Number"))
    phone2_mobile = models.BooleanField(default=False, verbose_name=_("Phone 2 Is Mobile"))
    service_location = models.ForeignKey(Location)
    billing_location = models.ForeignKey(Location, null=True, blank=True)
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)


    class Meta:
        db_table = 'customer'
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')


"""
class PhoneNumber(TimeStampedModel):
    is_mobile = models.BooleanField(default=False)
    number = models.CharField(max_length=15)

    class Meta:
        db_table = 'city'
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
"""