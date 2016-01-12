# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afc', '0002_auto_20160112_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendant',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]
