from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Creating ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	# Authenticating the  authentic user
	# authentication_classes = [BasicAuthentication]			# no need to write this line because it is already written in settings.py
	# permission_classes = [IsAuthenticated]



class StudentModelViewSet2(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	# Authenticating the all user
	authentication_classes = [BasicAuthentication]
	permission_classes=[AllowAny]