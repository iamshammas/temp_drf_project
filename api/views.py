# from django.http import JsonResponse
# from django.shortcuts import render
from .models import studentModel
from .serializers import studentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view (['GET'])
def studentsView(request):
    if request.method == 'GET':
        students = studentModel.objects.all()
        serializer = studentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
