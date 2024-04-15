from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BasePermission):
	def authenticate(self, request):
		username = request.GET.get('username')
		if username is None:
			return None
		
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			return AuthenticationFailed("No such User")
		return (user, None)
	
	def authenticate_header(self, request):
		return 'Token'