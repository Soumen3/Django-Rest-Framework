from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ['name', 'roll', 'city', "marks"]
	
	
	def create(self, validated_data):
		return Student.objects.create(**validated_data)