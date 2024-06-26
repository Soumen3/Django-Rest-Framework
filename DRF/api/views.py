from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.

# Model object - single student data
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    print('stu:',stu)
    serializer = StudentSerializer(stu)
    print('serializer:', serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# Model object - all student data
def student_list(request):
    stu=Student.objects.all()
    print('stu:',stu)
    serializer = StudentSerializer(stu, many=True)
    print('serializer:', serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')