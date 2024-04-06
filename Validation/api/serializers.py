from rest_framework import serializers
from .models import Student

# Validators
def start_with_r(value):
	if value[0].lower() != 'r':
		raise serializers.ValidationError('Name should be start with R')

class StudentSerializer(serializers.ModelSerializer):
	name = serializers.CharField(validators=[start_with_r])
	
	class Meta:
		model = Student
		fields = ['id', 'name', 'roll', 'city']

	
	def create(self, validated_data):
		return super().create(validated_data)
	
	def update(self, instance, validated_data):
		return super().update(instance, validated_data)
	

	# Field level validation
	def validate_roll(self, value):
		if value >= 200:
			raise serializers.ValidationError('Seat Full')
		return value
	
	# Object level validation
	def validate(self, data):
		nm = data.get('name')
		print("data : ",data)
		ct = data.get('city')
		if nm.lower() == 'pritam' and ct.lower() != 'durgapur':
			raise serializers.ValidationError('City must be Durgapur')
		return data
	
