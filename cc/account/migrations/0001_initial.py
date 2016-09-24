# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import cc.account.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('balance', cc.account.models.AmountField(default=Decimal('0'), max_digits=12, decimal_places=2)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CreditLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bal_mult', models.SmallIntegerField(choices=[(1, b'+1'), (-1, b'-1')])),
                ('limit', cc.account.models.AmountField(default=Decimal('0'), null=True, max_digits=12, decimal_places=2, blank=True)),
                ('account', models.ForeignKey(related_name='creditlines', to='account.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='creditline',
            name='node',
            field=models.ForeignKey(related_name='creditlines', to='account.Node'),
        ),
    ]
