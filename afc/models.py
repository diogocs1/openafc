# encoding: UTF-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# TODO: Adicionar ponto de atendimento (point_of_care)

class Address(models.Model):
	street_line_1 		= models.CharField(max_length=60)
	complement_line_2 	= models.CharField(max_length=60, blank=True)
	city				= models.CharField(max_length=60)
	state				= models.CharField(max_length=40)
	country				= models.CharField(max_length=40)


class Passenger(models.Model):
	cpf 		= models.CharField(max_length=11, unique=True)
	full_name 	= models.CharField(max_length=40)
	cell_phone 	= models.CharField(max_length=20)
	birth_date 	= models.DateField()
	user_id 	= models.OneToOneField(User, on_delete=models.CASCADE)
	address_id 	= models.OneToOneField('Address', on_delete=models.CASCADE)


class Company(models.Model):
	name 		= models.CharField(max_length=40)
	employee 	= models.CharField(max_length=40)
	cnpj 		= models.CharField(max_length=20, unique=True)
	phone 		= models.CharField(max_length=20)
	user_id 	= models.OneToOneField(User, on_delete=models.CASCADE)
	address_id 	= models.OneToOneField('Address', on_delete=models.CASCADE)


class Supervisor(models.Model):
	username 	= models.CharField(max_length=40, unique=True)
	full_name 	= models.CharField(max_length=40, unique=True)
	phone 		= models.CharField(max_length=20)
	user_id 	= models.OneToOneField(User, on_delete=models.CASCADE)
	address_id 	= models.OneToOneField('Address', on_delete=models.CASCADE)


class Point_of_care(models.Model):
	name 			= models.CharField(max_length=40)
	address_id 		= models.OneToOneField('Address', on_delete=models.CASCADE)
	supervisor_id	= models.ForeignKey('Supervisor')


class Attendant(models.Model):
	cpf 				= models.CharField(max_length=11, unique=True)
	full_name 			= models.CharField(max_length=40)
	cell_phone 			= models.CharField(max_length=20)
	user_id 			= models.OneToOneField(User, on_delete=models.CASCADE)
	point_of_care_id	= models.ForeignKey('Point_of_care')


class Validator(models.Model):
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
	created_by		= models.ForeignKey('Attendant')
	company_id 		= models.ForeignKey('Company', blank=True)


class Receipt(models.Model):
	date_time 		= models.DateTimeField(auto_now_add=True)
	ticket_id 		= models.ForeignKey('Ticket')
	validator_id 	= models.ForeignKey('Validator')