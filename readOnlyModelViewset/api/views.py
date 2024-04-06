from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# Creating ModelViewSet
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer