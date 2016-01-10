# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afc', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vehicle',
            new_name='Validator',
        ),
        migrations.RenameField(
            model_name='receipt',
            old_name='vehicle_id',
            new_name='validator_id',
        ),
    ]
