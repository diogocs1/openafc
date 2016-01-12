# encoding: UTF-8

from rest_framework import serializers, exceptions
from afc.models import *

from login.serializers import *


class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address


class UserModelSerializer(serializers.HyperlinkedModelSerializer):
	address_id = AddressSerializer()

	class Meta:
		abstract = True

	def create(self, validated_data):
		# If not user, create
		if not validated_data.has_key('user_id'):
			username = validated_data.get('cpf') or validated_data.get('cnpj') or validated_data.get('username')
			user_serializer = UserSerializer(data={'username': username})
			user_serializer.is_valid(raise_exception=True)
			validated_data['user_id'] = user_serializer.save()
		else:
			validated_data['user_id'].username = validated_data.get('cpf') or validated_data.get('cnpj') or validated_data.get('username')

		# Deserializing address_id
		address_data = validated_data.pop('address_id')
		addr = Address.objects.create(**address_data)
		validated_data['address_id'] = addr
		# Continue to Default create
		return super(UserModelSerializer, self).create(validated_data)

	def update(self, instance, validated_data):
		if validated_data.has_key('cpf') or validated_data.has_key('cnpj') or validated_data.has_key('username'):
			instance.user_id.username = validated_data.get('cpf') or validated_data.get('cnpj') or validated_data.get('username')
		return super(UserModelSerializer, self).update(instance, validated_data)


class PassengerSerializer(UserModelSerializer):
	class Meta:
		model = Passenger
		extra_kwargs = {
			'user_id':{
				'required': False
			}
		}


class CompanySerializer(UserModelSerializer):
	class Meta:
		model = Company
		extra_kwargs = {
			'user_id':{
				'required': False
			}
		}


class SupervisorSerializer(UserModelSerializer):
	class Meta:
		model = Supervisor
		extra_kwargs = {
			'user_id':{
				'required': False
			}
		}


class ValidatorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Validator
		extra_kwargs = {
			'company_id': {
				'required': False
			}
		}


class TicketSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ticket


class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Receipt


class PointOfCareSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Point_of_care


class AttendantSerializer(UserSerializer):
	class Meta:
		model = Attendant
		extra_kwargs = {
			'user_id':{
				'required': False
			}
		}