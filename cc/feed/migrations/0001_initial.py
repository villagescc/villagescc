# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(db_index=True)),
                ('item_type', models.CharField(max_length=16, choices=[(b'post', b'Post'), (b'profile', b'Profile Update'), (b'acknowledgement', b'Acknowledgement'), (b'endorsement', b'Endorsement')])),
                ('item_id', models.PositiveIntegerField()),
                ('public', models.BooleanField()),
                ('location', models.ForeignKey(blank=True, to='geo.Location', null=True)),
                ('poster', models.ForeignKey(related_name='posted_feed_items', to='profile.Profile')),
                ('recipient', models.ForeignKey(related_name='received_feed_items', blank=True, to='profile.Profile', null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='feeditem',
            unique_together=set([('item_type', 'item_id')]),
        ),
    ]
