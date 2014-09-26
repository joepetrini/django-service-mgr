# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('line1', models.CharField(max_length=200, verbose_name='Addressline 1')),
                ('line2', models.CharField(max_length=200, null=True, verbose_name='Addressline 2', blank=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
            ],
            options={
                'db_table': 'address',
                'verbose_name': 'Postal Address',
                'verbose_name_plural': 'Postal Addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=5)),
                ('state', models.CharField(default=b'NJ', max_length=2)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('poly', django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, blank=True)),
            ],
            options={
                'db_table': 'city',
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=5)),
                ('poly', django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, blank=True)),
            ],
            options={
                'db_table': 'zipcode',
                'verbose_name': 'Zip Code',
                'verbose_name_plural': 'Zip Codes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(to='location.City'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='zipcode',
            field=models.ForeignKey(to='location.Zipcode'),
            preserve_default=True,
        ),
    ]
