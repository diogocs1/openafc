# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_line_1', models.CharField(max_length=60)),
                ('complement_line_2', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpf', models.CharField(unique=True, max_length=11)),
                ('full_name', models.CharField(max_length=40)),
                ('cell_phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('employee', models.CharField(max_length=40)),
                ('cnpj', models.CharField(unique=True, max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('address_id', models.OneToOneField(to='afc.Address')),
                ('user_id', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpf', models.CharField(unique=True, max_length=11)),
                ('full_name', models.CharField(max_length=40)),
                ('cell_phone', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('address_id', models.OneToOneField(to='afc.Address')),
                ('user_id', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Point_of_care',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('address_id', models.OneToOneField(to='afc.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=40)),
                ('full_name', models.CharField(unique=True, max_length=40)),
                ('phone', models.CharField(max_length=20)),
                ('address_id', models.OneToOneField(to='afc.Address')),
                ('user_id', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=40)),
                ('cash', models.FloatField(default=0.0)),
                ('expires', models.DateTimeField()),
                ('cash_max', models.FloatField(default=1000.0)),
                ('company_id', models.ForeignKey(to='afc.Company', blank=True)),
                ('created_by', models.ForeignKey(to='afc.Attendant')),
                ('passenger_id', models.ForeignKey(to='afc.Passenger')),
            ],
        ),
        migrations.CreateModel(
            name='Validator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hardware_online', models.BooleanField(default=False)),
                ('vehicle_status', models.CharField(default=b'out', max_length=10, choices=[(b'transit', b'In transit'), (b'stop', b'Stopped'), (b'out', b'Out of service')])),
                ('location_lat', models.CharField(max_length=20, blank=True)),
                ('location_long', models.CharField(max_length=20, blank=True)),
                ('company_id', models.ForeignKey(to='afc.Company')),
            ],
        ),
        migrations.AddField(
            model_name='receipt',
            name='ticket_id',
            field=models.ForeignKey(to='afc.Ticket'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='validator_id',
            field=models.ForeignKey(to='afc.Validator'),
        ),
        migrations.AddField(
            model_name='point_of_care',
            name='supervisor_id',
            field=models.ForeignKey(to='afc.Supervisor'),
        ),
        migrations.AddField(
            model_name='attendant',
            name='point_of_care_id',
            field=models.ForeignKey(to='afc.Point_of_care'),
        ),
        migrations.AddField(
            model_name='attendant',
            name='user_id',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
