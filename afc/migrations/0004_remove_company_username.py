# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afc', '0003_auto_20160107_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='username',
        ),
    ]
