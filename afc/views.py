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
	permission_classes = [IsAdminSupervisorOrSelf]


class CompanyViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza empresas, Caso "user_id" não seja fornecido, é criado um novo usuário
	"""
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	permission_classes = [IsAdminSupervisorOrSelf]


class SupervisorViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza administradores de transporte, Caso "user_id" não seja fornecido, é criado um novo usuário
	"""
	queryset = Supervisor.objects.all()
	serializer_class = SupervisorSerializer
	permission_classes = [IsAdminOrSelf]


class ValidatorViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza veículos e o equipamento embarcado
	"""
	queryset = Validator.objects.all()
	serializer_class = ValidatorSerializer
	permission_classes = [IsAdminSupervisorCompanyOwner]

	def perform_create(self, serializer):
		if hasattr(self.request.user, 'company'):
			serializer.save(company_id=self.request.user.company)


class TicketViewSet(viewsets.ModelViewSet):
	"""
	Adiciona, edita e visualiza tickets de passagem
	"""
	queryset = Ticket.objects.all()
	serializer_class = TicketSerializer
	permission_classes = [IsAdminSupervisorAttendant]


class ReceiptViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	Cria e apaga recibos de pagamento de passagem
	"""
	queryset = Receipt.objects.all()
	serializer_class = ReceiptSerializer
	permission_classes = [PassengerIsOwner]


class PointOfCareViewSet(viewsets.ModelViewSet):
	"""
	Cria, edita e apaga Pontos de atendimento
	"""
	queryset = Point_of_care.objects.all()
	serializer_class = PointOfCareSerializer
	permission_classes = [IsAdminOrSupervisor]


class AttendantViewSet(viewsets.ModelViewSet):
	"""
	Cria, edita e apaga atententes de POC (Point of Care)
	"""
	queryset = Attendant.objects.all()
	serializer_class = AttendantSerializer
	permissions = [IsAdminSupervisorManager]