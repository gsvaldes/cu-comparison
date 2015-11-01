# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default=b'Austin', max_length=100),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(default=b'Texas', max_length=100),
        ),
        migrations.AddField(
            model_name='location',
            name='zip_code',
            field=models.CharField(default=b'', max_length=5),
        ),
        migrations.AlterField(
            model_name='location',
            name='business',
            field=models.ForeignKey(verbose_name=b'business_location', to='locator.Company'),
        ),
    ]
