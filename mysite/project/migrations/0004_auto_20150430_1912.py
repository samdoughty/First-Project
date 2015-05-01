# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0003_auto_20150427_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='FirstName',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='LastName',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='UserID',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
    ]
