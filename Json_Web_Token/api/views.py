from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.custompermissions import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# Creating ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	authentication_classes = [JWTAuthentication]
	permission_classes = [JWTAuthentication]


