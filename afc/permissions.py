# encoding: UTF-8

from rest_framework import permissions


class IsAdminSupervisorCompanyOwner(permissions.BasePermission):
	def has_permission(self, request, view):
		# is Admin, Supervisor or Company?
		return request.user.is_staff or hasattr(request.user, 'supervisor') or hasattr(request.user, 'company')

	def has_object_permission(self, request, view, obj):
		# Company is owner?
		if hasattr(obj, 'company_id') and hasattr(request.user, 'company'):
			return obj.company_id == request.user.company or request.user.is_staff or hasattr(request.user, 'supervisor')


class IsAdminSupervisorAttendant(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user.is_staff or hasattr(request.user, 'supervisor') or hasattr(request.user, 'attendant')


class IsAdminSupervisorOrSelf(permissions.BasePermission):
	def has_permission(self, request, view):
		# is Admin or Supervisor?
		return request.user.is_staff or hasattr(request.user, 'supervisor')

	def has_object_permission(self, request, view, obj):
		# is Self?, admin or supervisor?
		if hasattr(obj, 'user_id'):
			return obj.user_id == request.user or self.has_permission(request, view)


class IsAdminOrSelf(permissions.BasePermission):
	def has_permission(self, request, view):
		# is Admin or Supervisor?
		return request.user.is_staff

	def has_object_permission(self, request, view, obj):
		# is Self?, admin or supervisor?
		if hasattr(obj, 'user_id'):
			return obj.user_id == request.user or self.has_permission(request, view)


class IsAdminSupervisorManager(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user.is_staff or hasattr(request.user, 'supervisor') or (hasattr(request.user, 'attendant') and request.user.attendant.is_manager)


class IsAdminOrSupervisor(permissions.BasePermission):
	def has_permission(self, request, view):
		# is Admin or Supervisor?
		return request.user.is_staff or hasattr(request.user, 'supervisor')

	def has_object_permission(self, request, view, obj):
		return self.has_permission(request, view)


class PassengerIsOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if hasattr(obj, 'passenger_id') and hasattr(request.user, 'passenger'):
			return obj.passenger_id == request.user.passenger