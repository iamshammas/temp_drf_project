# from django.http import JsonResponse
# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import studentModel
from .serializers import studentSerializer,employeeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from employee.models import employeeModel
from rest_framework.views import APIView

# from api import serializers

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
    
@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,pk):
    student = get_object_or_404(studentModel,pk=pk)
    if request.method == 'GET':
        serializers = studentSerializer(student)
        print(student)
        print(serializers.data)
        return Response(serializers.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializers = studentSerializer(student,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#   EMPLOYEES

class employeeView(APIView):
    def get(self,request):
        employees = employeeModel.objects.all()
        serializers = employeeSerializer(employees,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)