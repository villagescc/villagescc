# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cc.account.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', cc.account.models.AmountField(max_digits=12, decimal_places=2)),
                ('new_balance', cc.account.models.AmountField(max_digits=12, decimal_places=2)),
                ('account', models.ForeignKey(related_name='entries', to='account.Account')),
            ],
            options={
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', cc.account.models.AmountField(max_digits=12, decimal_places=2)),
                ('memo', models.TextField(blank=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('last_attempted_at', models.DateTimeField(null=True)),
                ('status', models.CharField(default=b'pending', max_length=16, choices=[(b'pending', b'Pending'), (b'completed', b'Completed'), (b'failed', b'Failed')])),
                ('payer', models.ForeignKey(related_name='sent_payments', to='account.Node')),
                ('recipient', models.ForeignKey(related_name='received_payments', to='account.Node')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='payment',
            field=models.ForeignKey(related_name='entries', to='payment.Payment'),
        ),
    ]
