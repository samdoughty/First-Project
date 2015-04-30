# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20150427_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropzone',
            name='pictureID',
            field=models.ForeignKey(null=True, blank=True, to='project.Picture'),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='pictureID',
            field=models.ForeignKey(null=True, blank=True, to='project.Picture'),
        ),
        migrations.AlterField(
            model_name='jump',
            name='VideoResourceID',
            field=models.ForeignKey(null=True, blank=True, to='project.VideoResource'),
        ),
        migrations.AlterField(
            model_name='jumptype',
            name='pictureID',
            field=models.ForeignKey(null=True, blank=True, to='project.Picture'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='PictureID',
            field=models.ForeignKey(null=True, blank=True, to='project.Picture'),
        ),
    ]
