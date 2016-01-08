# encoding: UTF-8

from rest_framework import serializers, exceptions
from afc.models import *

from login.serializers import *


class UserModelSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		abstract = True

	def create(self, validated_data):
		# Se o usuário não for passado, crie um novo
		if not validated_data.has_key('user_id'):
			if validated_data.has_key('cpf'):
				username = validated_data['cpf']
			elif validated_data.has_key('cnpj'):
				username = validated_data['cnpj']
			else:
				username = validated_data['username']
			user_serializer = UserSerializer(data={'username': username})
			user_serializer.is_valid(raise_exception=True)
			validated_data['user_id'] = user_serializer.save()
		else:
			validated_data['user_id'].username = validated_data['cpf']
		# Verifica se o usuário é válido
		return super(UserModelSerializer, self).create(validated_data)

	def update(self, instance, validated_data):
		if validated_data.has_key('cpf'):
			instance.user_id.username = validated_data['cpf']
		elif validated_data.has_key('cnpj'):
			instance.user_id.username = validated_data['cnpj']
		elif validated_data.has_key('username'):
			instance.user_id.username = validated_data['username']
		return super(UserModelSerializer, self).update(instance, validated_data)


class PassengerSerializer(UserModelSerializer):
	class Meta:
		model = Passenger
		fields = ['cpf', 'full_name', 'cell_phone', 'birth_date', 'user_id', 'url']
		extra_kwargs = {
			'user_id':{
				'required': False
			}
		}


class CompanySerializer(UserModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'
		extra_kwargs = {
			'user_id':{
				'required': False
			}
		}


class SupervisorSerializer(UserModelSerializer):
	class Meta:
		model = Supervisor
		fields = '__all__'
		extra_kwargs = {
			'user_id':{
				'required': False
			}
		}


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Vehicle
		fields = '__all__'


class TicketSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ticket
		fields = '__all__'


class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Receipt
		fields = '__all__'