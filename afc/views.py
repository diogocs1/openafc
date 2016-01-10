# encoding: UTF-8
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from afc.models import *
from afc.serializers import *
from afc.permissions import *


class PassengerViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza usuários passageiros. Caso "user_id" não seja fornecido, é criado um novo usuário
	"""
	queryset = Passenger.objects.all()
	serializer_class = PassengerSerializer
	permission_classes = [IsAdminUser or IsSupervisor or IsOwnerOrSelf]


class CompanyViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza empresas, Caso "user_id" não seja fornecido, é criado um novo usuário
	"""
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	permission_classes = [IsAdminUser or IsSupervisor or IsOwnerOrSelf]


class SupervisorViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza administradores de transporte, Caso "user_id" não seja fornecido, é criado um novo usuário
	"""
	queryset = Supervisor.objects.all()
	serializer_class = SupervisorSerializer
	permission_classes = [IsAdminUser or IsOwnerOrSelf]


class ValidatorViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza veículos e o equipamento embarcado
	"""
	queryset = Validator.objects.all()
	serializer_class = ValidatorSerializer
	permission_classes = [IsAdminUser or IsSupervisor or IsCompany and CompanyIsOwner]


class TicketViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	Adiciona, edita e visualiza tickets de passagem
	"""
	queryset = Ticket.objects.all()
	serializer_class = TicketSerializer
	permission_classes = [IsAdminUser or IsSupervisor]


class ReceiptViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	Cria e apaga recibos de pagamento de passagem
	"""
	queryset = Receipt.objects.all()
	serializer_class = ReceiptSerializer