# encoding: UTF-8

from rest_framework import permissions


class IsOwnerOrSelf(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return hasattr(obj, 'user_id') and obj.user_id == request.user


class IsSupervisor(permissions.BasePermission):
	def has_permission(self, request, view):
		return hasattr(request.user, 'supervisor') 


class IsPassenger(permissions.BasePermission):
	def has_parmission(self, request, view):
		return hasattr(request, 'user') and hasattr(request.user, 'passenger')


class IsCompany(permissions.BasePermission):
	def has_permission(self, request, view):
		return hasattr(request, 'user') and hasattr(request.user, 'company')


class CompanyIsOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if hasattr(obj, 'company_id') and hasattr(request, 'user') and hasattr(request.user, 'company'):
			return obj.company_id == request.user.company


class PassengerIsOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if hasattr(obj, 'passenger_id') and hasattr(request, 'user') and hasattr(request.user, 'passenger'):
			return obj.passenger_id == request.user.passenger