# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0002_auto_20151101_1946'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company',
            new_name='Business',
        ),
    ]
