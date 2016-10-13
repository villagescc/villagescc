# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cc.general.models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True)),
                ('country', cc.general.models.VarCharField(max_length=1000000000, verbose_name='Country')),
                ('state', cc.general.models.VarCharField(max_length=1000000000, verbose_name='State/Province (Abbr.)', blank=True)),
                ('city', cc.general.models.VarCharField(max_length=1000000000, verbose_name='City', blank=True)),
                ('neighborhood', cc.general.models.VarCharField(max_length=1000000000, verbose_name='Neighbourhood', blank=True)),
            ],
        ),
    ]
