from .models import studentModel
from rest_framework import serializers

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = '__all__'