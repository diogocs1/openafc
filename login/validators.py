# encoding: UTF-8

from django.core.exceptions import 	ValidationError
from OpenAFC import settings

import re


def validate_password(password):
	"""
	Validate password algorithm
	"""
	decimal = re.compile('^[0-9]+$')
	letter = re.compile('^[a-zA-Z]+$')

	if len(password) < settings.PASSWORD_LENGHT:
		return "Password lenght must be equal or longer to %d" % settings.PASSWORD_LENGHT
	elif decimal.match(password) or letter.match(password):
		return 'Password must be numbers and letters'
	return False