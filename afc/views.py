# encoding: UTF-8
from django.shortcuts import render

from rest_framework import viewsets

from afc.models import *
from afc.serializers import *


class PassengerViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza usuários passageiros. Caso "user_id" não seja fornecido, é criado um novo usuário
	"""
	queryset = Passenger.objects.all()
	serializer_class = PassengerSerializer


class CompanyViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza empresas, Caso "user_id" não seja fornecido, é criado um novo usuário
	"""
	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class SupervisorViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza administradores de transporte, Caso "user_id" não seja fornecido, é criado um novo usuário
	"""
	queryset = Supervisor.objects.all()
	serializer_class = SupervisorSerializer


class VehicleViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza veículos e o equipamento embarcado
	"""
	queryset = Vehicle.objects.all()
	serializer_class = VehicleSerializer


class TicketViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza tickets de passagem
	"""
	queryset = Ticket.objects.all()
	serializer_class = TicketSerializer


class ReceiptViewSet(viewsets.ModelViewSet):
	"""
	Cria e apaga recibos de pagamento de passagem
	"""
	queryset = Receipt.objects.all()
	serializer_class = ReceiptSerializer