# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dropzone',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('DropzoneName', models.CharField(max_length=50)),
                ('TheDescription', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(max_length=50)),
                ('TheDescription', models.CharField(max_length=1000)),
                ('StartDate', models.DateTimeField(verbose_name='start date')),
                ('EndDate', models.DateTimeField(verbose_name='end date')),
                ('Spaces', models.IntegerField(default=0)),
                ('DropzoneID', models.ForeignKey(to='project.Dropzone')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('EventTypeName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jump',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('ShortDescription', models.CharField(max_length=100)),
                ('TheDescription', models.CharField(max_length=1000)),
                ('Notes', models.CharField(max_length=1000)),
                ('JumpDate', models.DateTimeField(verbose_name='jump date')),
            ],
        ),
        migrations.CreateModel(
            name='JumpType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('JumpTypeName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(max_length=1000)),
                ('Verified', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=50)),
                ('TheDescription', models.CharField(max_length=1000)),
                ('PictureID', models.ForeignKey(to='project.Picture')),
            ],
        ),
        migrations.CreateModel(
            name='UserBooking',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('BookingDate', models.DateTimeField(verbose_name='booking date')),
            ],
        ),
        migrations.CreateModel(
            name='UserBookingEventProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('EventID', models.ForeignKey(to='project.Event')),
                ('ProductID', models.ForeignKey(to='project.Product')),
            ],
        ),
        migrations.CreateModel(
            name='UserJump',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('JumpNumber', models.IntegerField()),
                ('isOwner', models.BooleanField()),
                ('JumpID', models.ForeignKey(to='project.Jump')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VideoResource',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(max_length=1000)),
                ('Verified', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='userjump',
            name='UserProfileID',
            field=models.ForeignKey(to='project.UserProfile'),
        ),
        migrations.AddField(
            model_name='userbooking',
            name='EventProductID',
            field=models.ForeignKey(to='project.UserBookingEventProduct'),
        ),
        migrations.AddField(
            model_name='userbooking',
            name='UserProfileID',
            field=models.ForeignKey(to='project.UserProfile'),
        ),
        migrations.AddField(
            model_name='product',
            name='ProductTypeID',
            field=models.ForeignKey(to='project.ProductType'),
        ),
        migrations.AddField(
            model_name='jumptype',
            name='pictureID',
            field=models.ForeignKey(to='project.Picture'),
        ),
        migrations.AddField(
            model_name='jump',
            name='JumpTypeID',
            field=models.ForeignKey(to='project.JumpType'),
        ),
        migrations.AddField(
            model_name='jump',
            name='VideoResourceID',
            field=models.ForeignKey(to='project.VideoResource'),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='pictureID',
            field=models.ForeignKey(to='project.Picture'),
        ),
        migrations.AddField(
            model_name='event',
            name='EventTypeID',
            field=models.ForeignKey(to='project.EventType'),
        ),
        migrations.AddField(
            model_name='dropzone',
            name='pictureID',
            field=models.ForeignKey(to='project.Picture'),
        ),
    ]
