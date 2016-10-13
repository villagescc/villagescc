# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endorsement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.PositiveIntegerField(help_text="Each heart represents an hour of value you'd provide in exchange for acknowledgements.", verbose_name='Hearts')),
                ('text', models.TextField(verbose_name='Testimonial', blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('endorser', models.ForeignKey(related_name='endorsements_made', to='profile.Profile')),
                ('recipient', models.ForeignKey(related_name='endorsements_received', to='profile.Profile')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='endorsement',
            unique_together=set([('endorser', 'recipient')]),
        ),
    ]
