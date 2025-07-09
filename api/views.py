# from django.http import JsonResponse
# from django.shortcuts import render
from .models import studentModel
from .serializers import studentSerializer
from rest_framework import serializers,status
from rest_framework.response import Response

# Create your views here.

def studentsView(request):
    students = studentModel.objects.all()
    serializers = studentSerializer(students,many=True)
    return Response(serializers.data,status=status.HTTP_200_OK)