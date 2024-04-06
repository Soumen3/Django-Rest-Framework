from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ['id', 'name', 'roll', 'city', 'marks']

	def create(self, validated_data):
		return super().create(validated_data)
	
	def update(self, instance, validated_data):
		return super().update(instance, validated_data)