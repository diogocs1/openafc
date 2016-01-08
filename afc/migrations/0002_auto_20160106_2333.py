# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('afc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='user_id',
            field=models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
