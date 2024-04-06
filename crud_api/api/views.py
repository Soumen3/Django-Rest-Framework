from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def studetn_api(request):
	if request.method == 'GET':
		json_data = request.body
		print("Json_data : ",json_data)
		print("Type of Json_data : ",type(json_data))

		stream = io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)
		print("Python_data : ",python_data)
		print("Type of Python_data : ",type(python_data))

		id = python_data.get('id', None)
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			print("Serializer : ",serializer.data)
			print("Type of Serializer : ",type(serializer.data))
			return JsonResponse(serializer.data)
		
		stu = Student.objects.all()
		print("Student : ",stu)
		print("Type of Student : ",type(stu))
		serializer = StudentSerializer(stu, many=True)
		return JsonResponse(serializer.data, safe=False)
	
	elif request.method == 'POST':
		json_data = request.body
		print("Json_data : ",json_data)
		print("Type of Json_data : ",type(json_data))

		stream = io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)
		print("Python_data : ",python_data)
		print("Type of Python_data : ",type(python_data))

		serializer = StudentSerializer(data=python_data)
		if serializer.is_valid():
			serializer.save()
			msg = {'msg': 'Data Created'}
			return JsonResponse(msg)
		return JsonResponse(serializer.errors)

	elif request.method == 'PUT':
		json_data = request.body
		print("Json_data : ",json_data)
		print("Type of Json_data : ",type(json_data))

		stream = io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)
		print("Python_data : ",python_data)
		print("Type of Python_data : ",type(python_data))

		id = python_data.get('id')
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=python_data, partial=True)
		if serializer.is_valid():
			serializer.save()
			msg = {'msg': 'Data Updated'}
			return JsonResponse(msg)
		return JsonResponse(serializer.errors)
	
	elif request.method == 'DELETE':
		json_data = request.body
		print("Json_data : ",json_data)
		print("Type of Json_data : ",type(json_data))

		stream = io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)
		print("Python_data : ",python_data)
		print("Type of Python_data : ",type(python_data))

		id = python_data.get('id')
		stu = Student.objects.get(id=id)
		stu.delete()
		msg = {'msg': 'Data Deleted'}
		return JsonResponse(msg)
