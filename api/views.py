# from django.http import JsonResponse
# from django.shortcuts import render
from .models import studentModel
from .serializers import studentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view (['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        students = studentModel.objects.all()
        serializer = studentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)