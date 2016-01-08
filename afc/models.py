# encoding: UTF-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Passenger(models.Model):
	cpf 		= models.CharField(max_length=11, unique=True)
	full_name 	= models.CharField(max_length=40)
	cell_phone 	= models.CharField(max_length=20)
	birth_date 	= models.DateField()
	user_id 	= models.OneToOneField(User, on_delete=models.CASCADE)

class Company(models.Model):
	name 		= models.CharField(max_length=40)
	employee 	= models.CharField(max_length=40)
	cnpj 		= models.CharField(max_length=20, unique=True)
	phone 		= models.CharField(max_length=20)
	user_id 	= models.OneToOneField(User, on_delete=models.CASCADE)


class Supervisor(models.Model):
	username 	= models.CharField(max_length=40, unique=True)
	name 		= models.CharField(max_length=40, unique=True)
	phone 		= models.CharField(max_length=20)
	user_id 	= models.OneToOneField(User, on_delete=models.CASCADE)


class Vehicle(models.Model):
	hardware_online = models.BooleanField(blank=True, default=False)
	vehicle_status 	= models.CharField(max_length=10, default='out',
			choices=[('transit', 'In transit'), ('stop', 'Stopped'), ('out', 'Out of service')]
	)
	location_lat 	= models.CharField(max_length=20, blank=True)
	location_long 	= models.CharField(max_length=20, blank=True)
	company_id 		= models.ForeignKey('Company')


class Ticket(models.Model):
	type 			= models.CharField(max_length=40)
	cash 			= models.FloatField(default=0.0)
	expires 		= models.DateTimeField()
	cash_max 		= models.FloatField(default=1000.0)
	passenger_id 	= models.ForeignKey('Passenger')
	company_id 		= models.ForeignKey('Company', blank=True)


class Receipt(models.Model):
	date_time 	= models.DateTimeField(auto_now_add=True)
	ticket_id 	= models.ForeignKey('Ticket')
	vehicle_id 	= models.ForeignKey('Vehicle')