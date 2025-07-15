from .models import studentModel
from employee.models import employeeModel
from rest_framework import serializers
from staff.models import staffModel

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = '__all__'

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employeeModel
        fields = '__all__'

class staffSerializer(serializers.ModelSerializer):
    class Meta:
       model = staffModel
       fields = '__all__'