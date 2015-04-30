# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropzone',
            name='pictureID',
            field=models.ForeignKey(to='project.Picture', null=True),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='pictureID',
            field=models.ForeignKey(to='project.Picture', null=True),
        ),
        migrations.AlterField(
            model_name='jump',
            name='VideoResourceID',
            field=models.ForeignKey(to='project.VideoResource', null=True),
        ),
        migrations.AlterField(
            model_name='jumptype',
            name='pictureID',
            field=models.ForeignKey(to='project.Picture', null=True),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='PictureID',
            field=models.ForeignKey(to='project.Picture', null=True),
        ),
    ]
