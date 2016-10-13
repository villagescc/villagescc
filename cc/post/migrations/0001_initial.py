# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cc.general.models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', cc.general.models.VarCharField(max_length=100, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('image', models.ImageField(upload_to=b'post/%Y/%m', max_length=256, verbose_name='Image', blank=True)),
                ('want', models.BooleanField(default=False, help_text='Leave unchecked if your post is an offer.', verbose_name='Want')),
                ('location', models.ForeignKey(to='geo.Location')),
                ('user', models.ForeignKey(related_name='posts', to='profile.Profile')),
            ],
        ),
    ]
