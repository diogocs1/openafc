# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='complement_line_2',
            field=models.CharField(max_length=60, blank=True),
        ),
    ]
