# GenericApiView and model Mixin

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


# List and Create = PK is not required
class ListCreateStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
	queryset= Student.objects.all()
	serializer_class = StudentSerializer

	def get(self, request, *args, **kwargs):
		get_data= self.list(request, *args, **kwargs)
		# print("GET METHOD: ", get_data)
		# print("GET METHOD type", type(get_data))
		# print("GET METHOD data: ", get_data.data)
		# print("GET METHOD data type: ", type(get_data.data))
		return get_data
	
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

# Retrive Update and Destroy = PK is required
class RetriveUpdateDestroyStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
	queryset= Student.objects.all()
	serializer_class = StudentSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)
	
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
