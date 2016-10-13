# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cc.general.models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('to_email', cc.general.models.EmailField(max_length=254, verbose_name="Friend's email")),
                ('endorsement_weight', models.PositiveIntegerField(help_text="Each heart represents an hour of value you'd provide in exchange for acknowledgements.", verbose_name='Hearts')),
                ('endorsement_text', models.TextField(verbose_name='Testimonial', blank=True)),
                ('message', models.TextField(help_text='Sent with the invitation email only. Not public.', verbose_name='Private message', blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('code', cc.general.models.VarCharField(unique=True, max_length=1000000000)),
            ],
        ),
        migrations.CreateModel(
            name='PasswordResetLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', cc.general.models.VarCharField(unique=True, max_length=1000000000)),
                ('expires', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', cc.general.models.VarCharField(max_length=1000000000, verbose_name='Name', blank=True)),
                ('photo', models.ImageField(upload_to=b'user/%Y/%m', max_length=256, verbose_name='Photo', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(blank=True, to='geo.Location', null=True)),
                ('trusted_profiles', models.ManyToManyField(related_name='trusting_profiles', to='profile.Profile', blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', cc.general.models.EmailField(max_length=254, blank=True)),
                ('endorsement_limited', models.BooleanField(default=True, help_text="Uncheck this if you know what you're doing and want to give out more hearts.", verbose_name='Limited hearts')),
                ('send_notifications', models.BooleanField(default=True, help_text='Receive email whenever someone endorses or acknowledges you.', verbose_name='Receive notifications')),
                ('send_newsletter', models.BooleanField(default=True, help_text='Receive occasional news about the Villages community.', verbose_name='Receive updates')),
                ('language', cc.general.models.VarCharField(default=b'en', max_length=8, verbose_name='Language', choices=[(b'en', 'English'), (b'fi', 'suomi'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'es', 'espa\xf1ol'), (b'de', 'Deutsch'), (b'it', 'italiano'), (b'fr', 'fran\xe7ais')])),
                ('feed_radius', models.IntegerField(null=True, blank=True)),
                ('feed_trusted', models.BooleanField(default=False)),
                ('profile', models.OneToOneField(related_name='settings', to='profile.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='passwordresetlink',
            name='profile',
            field=models.ForeignKey(to='profile.Profile'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='from_profile',
            field=models.ForeignKey(related_name='invitations_sent', to='profile.Profile'),
        ),
    ]
