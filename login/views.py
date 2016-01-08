# encoding: UTF-8

from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError

from rest_framework import viewsets, permissions, exceptions, serializers
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from login.serializers import UserSerializer, GroupSerializer
from login.validators import validate_password


class UserViewSet(viewsets.ModelViewSet):
	"""
	Habilita a visualização e edição de usuários.
	Para definir uma nova senha, use o Endpoint  POST: /users/{id}/set_password
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

	@detail_route(methods=['post'], permission_classes=[permissions.IsAdminUser])
	def set_password(self, request, *args, **kwargs):
		"""
		Cria uma nova senha para o Usuário
		@param: password:String
		@return: status : dict/JSON
		"""
		user = self.get_object()
		password = request.data['password']

		error = validate_password(password)
		if error:
			raise serializers.ValidationError({'error':error})
		user.set_password(password)
		user.save()
		return Response({'status': 'Password is set'})


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	Habilita a visualização e edição de grupos de permissões
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer