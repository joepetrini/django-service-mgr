from django.utils.translation import ugettext as _
from django.contrib.gis.db import models


class Zipcode(models.Model):
    code = models.CharField(max_length=5)
    poly = models.PolygonField()
    objects = models.GeoManager()

    class Meta:
        db_table = 'zipcode'
        verbose_name = _('Zip Code')
        verbose_name_plural = _('Zip Codes')


class City(models.Model):
    name = models.CharField(max_length=5)
    state = models.CharField(max_length=2, default="NJ")
    point = models.PointField()
    poly = models.PolygonField()
    objects = models.GeoManager()

    class Meta:
        db_table = 'city'
        verbose_name = _('City')
        verbose_name_plural = _('Cities')



class Address(models.Model):
    line1 = models.CharField(max_length=200, verbose_name = _("Addressline 1"))
    line2 = models.CharField(max_length=200, verbose_name = _("Addressline 2"), blank=True, null=True)
    zipcode = models.ForeignKey(Zipcode)
    city = models.ForeignKey(City)
    point = models.PointField()

    class Meta:
        db_table = 'address'
        verbose_name = _('Postal Address')
        verbose_name_plural = _('Postal Address')