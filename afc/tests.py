# encoding: UTF-8
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from afc.models import *


class PassengerTests(APITestCase):
	def setUp(self):
		self.response = None
		self.url = reverse('passenger-list')
		self.user = User(**{
			'username': 'admin',
			'password': 'admin'
		})
		self.user.save()
		self.client.force_authenticate(user=self.user)

		passenger = {
			"cpf": "09160162422",
			"full_name": "Diogo Cabral da Silva",
			"cell_phone": "82996374800",
			'birth_date': '1993-06-14'
		}
		# Cria um novo passageiro
		self.passenger = self.client.post(self.url, passenger, format='json')

	def test_admin_update_passenger(self):
		"""
		Ensure we update a new Passenger / User object
		"""
		passenger_update = {
			'cpf': '12345678901'
		}
		# Altera o passageiro criado anteriormente
		self.response = self.client.patch(self.passenger.data['url'], passenger_update, format='json')
		self.assertEqual(self.response.status_code, status.HTTP_200_OK)

	def test_passenger_create_passenger(self):
		"""
		Ensure passenger create another passenger
		"""
		user = User.objects.get(username='09160162422')
		# self.client.force_authenticate(user=user)

		another_passenger = {
			"cpf": "232332",
			"full_name": "Another Passenger",
			"cell_phone": "82996374800",
			'birth_date': '1993-06-14'
		}

		self.response = self.client.post(self.url, another_passenger)
		self.assertEqual(self.response.status_code, status.HTTP_401_UNAUTHORIZED)