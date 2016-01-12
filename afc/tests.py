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
			'password': 'admin',
			'is_staff': True
		})
		self.user.save()
		self.client.force_authenticate(user=self.user)

		passenger = {
			"cpf": "09160162422",
			"full_name": "Diogo Cabral da Silva",
			"cell_phone": "82996374800",
			'birth_date': '1993-06-14',
			"address_id": {
				"street_line_1": "Rua 15",
				'complement_line_2': '',
				'city': "Arapiraca",
				"state": "Alagoas",
				"country": "Brasil"
			}
		}

		# Cria um novo passageiro
		self.passenger = self.client.post(self.url, passenger)

	def test_admin_update_passenger(self):
		"""
		Ensure we update a new Passenger / User object
		"""
		self.assertEqual(self.passenger.status_code, status.HTTP_201_CREATED)

		passenger_update = {
			'cpf': '12345678901'
		}
		# Altera o passageiro criado anteriormente
		self.response = self.client.patch(self.passenger.data['url'], passenger_update, format='json')
		self.assertEqual(self.response.status_code, status.HTTP_200_OK)

	def test_passenger_create_passenger(self):
		"""
		Ensure passenger cannot create another passenger
		"""
		self.assertEqual(self.passenger.status_code, status.HTTP_201_CREATED)

		user = User.objects.get(username='09160162422')
		self.client.force_authenticate(user=user)

		another_passenger = {
			"cpf": "232332",
			"full_name": "Another Passenger",
			"cell_phone": "82996374800",
			'birth_date': '1993-06-14',
			"address_id": {
				"street_line_1": "Rua 15",
				'complement_line_2': '',
				'city': "Arapiraca",
				"state": "Alagoas",
				"country": "Brasil"
			}
		}

		self.response = self.client.post(self.url, another_passenger)
		self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)


class SupervisorTests(APITestCase):
	def setUp(self):
		# Creating Admin
		self.user = User(**{
			'username': 'admin',
			'password': 'admin',
			'is_staff': True
		})
		self.user.save()
		self.client.force_authenticate(user=self.user)
		# Creating Supervisor
		supervisor = {
			"username": "jose",
			"full_name": "José",
			"phone": "8299123445",
			"address_id": {
				"street_line_1": "Rua 15",
				'complement_line_2': '',
				'city': "Arapiraca",
				"state": "Alagoas",
				"country": "Brasil"
			}
		}
		self.url = reverse('supervisor-list')

		self.response = self.client.post(self.url, supervisor)

		user = User.objects.get(username=supervisor['username'])
		self.client.force_authenticate(user=user)

	def test_supervisor_create_company(self):
		"""
		Ensure supervisor can create company
		"""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

		company = {
			"name": "VIAÇÃO BOM FIM",
			"employee": "encarregado 1",
			"cnpj": "0987654321",
			"phone": "121221212",
			"address_id": {
				"street_line_1": "Rua 15",
				'complement_line_2': '',
				'city': "Arapiraca",
				"state": "Alagoas",
				"country": "Brasil"
			}
		}
		company_url = reverse('company-list')
		response = self.client.post(company_url, company)
		# print response.data
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_supervisor_create_supervisor(self):
		"""
		Ensure supervisor can't create another supervisor
		"""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

		another_supervisor = {
			"username": "santos",
			"full_name": "Santos",
			"phone": "8212344567",
			"address_id": {
				"street_line_1": "Rua 15",
				'complement_line_2': '',
				'city': "Arapiraca",
				"state": "Alagoas",
				"country": "Brasil"
			}
		}
		self.response = self.client.post(self.url, another_supervisor)
		self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

	def test_supervisor_create_passenger(self):
		"""
		Ensure supervisor can create passenger
		"""
		another_passenger = {
			"cpf": "232332",
			"full_name": "Another Passenger",
			"cell_phone": "82996374800",
			'birth_date': '1993-06-14',
			"address_id": {
				"street_line_1": "Rua 15",
				'complement_line_2': '',
				'city': "Arapiraca",
				"state": "Alagoas",
				"country": "Brasil"
			}
		}

		self.client.post(self.url, another_passenger)
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class CompanyTests(APITestCase):
	def setUp(self):
		# Creating Admin
		self.url = reverse('company-list')
		user = User(**{
			'username': 'admin',
			'password': 'admin',
			'is_staff': True
		})
		user.save()
		self.client.force_authenticate(user=user)

		company = {
			"name": "VIAÇÃO ROTA",
			"employee": "encarregado 1",
			"cnpj": "1234567890",
			"phone": "121221212",
			"address_id": {
				"street_line_1": "Rua 15",
				'complement_line_2': '',
				'city': "Arapiraca",
				"state": "Alagoas",
				"country": "Brasil"
			}
		}
		response = self.client.post(self.url, company)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		user = User.objects.get(username=company['cnpj'])
		self.client.force_authenticate(user=user)

	def test_company_create_company(self):
		"""
		Ensure company con't create another company
		"""
		another_company = {
			"name": "VIAÇÃO BOMFIM",
			"employee": "encarregado 1",
			"cnpj": "0987654321",
			"phone": "121221212",
			"address_id": {
				"street_line_1": "Rua 15",
				'complement_line_2': '',
				'city': "Arapiraca",
				"state": "Alagoas",
				"country": "Brasil"
			}
		}
		response = self.client.post(self.url, another_company)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

	def test_company_create_validator(self):
		"""
		Ensure company can create Validators
		"""
		url = reverse('validator-list')
		validator = {
			"hardware_online": True,
			"vehicle_dtatus": "transit"
		}
		response = self.client.post(url, validator)
		
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_company_create_passenger(self):
		"""
		Ensure company can create Passengers
		"""
		url = reverse('passenger-list')
		passenger = {
			"cpf": "232332",
			"full_name": "Another Passenger",
			"cell_phone": "82996374800",
			'birth_date': '1993-06-14',
			"address_id": {
				"street_line_1": "Rua 15",
				'complement_line_2': '',
				'city': "Arapiraca",
				"state": "Alagoas",
				"country": "Brasil"
			}
		}
		response = self.client.post(url, passenger)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)