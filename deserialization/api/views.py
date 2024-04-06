
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt    # This decorator is used to disable csrf token
def student_create(request):
    if request.method == 'POST':
        json_data= request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print("python data: ", python_data)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            return JsonResponse(res)
        
        return JsonResponse(serializer.errors)