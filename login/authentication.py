# encoding: UTF-8

from rest_framework import authentication


class PassengerAuthentication(authentication.BaseAuthentication):
	"""
	Backend para autenticação de passageiros
	"""
	def authenticate(self, request):
		print 
		print request
		print 

		return ('','')