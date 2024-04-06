from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST'])
def hello_world(request):
	if request.method == 'GET':
		return Response({"message": "This is get request"})

	if request.method == "POST":
		print(request.data)
		print("Type of request.data: ", type(request.data))
		return Response({"message": "This is post request", "data": request.data})