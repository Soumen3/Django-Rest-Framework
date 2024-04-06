from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
# Creating ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	# Authenticating the  authentic user
	authentication_classes = [SessionAuthentication]			# no need to write this line because it is already written in settings.py
	# permission_classes = [IsAuthenticated]
	# permission_classes=[IsAdminUser]
	# permission_classes=[AllowAny]
	# permission_classes=[IsAuthenticatedOrReadOnly]
	# permission_classes=[DjangoModelPermissions]
	permission_classes=[DjangoModelPermissionsOrAnonReadOnly]



class StudentModelViewSet2(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	# Authenticating the all user
	# authentication_classes = [BasicAuthentication]
	permission_classes=[AllowAny]