from django.http import JsonResponse
from django.shortcuts import render
from .models import studentModel

# Create your views here.

def studentsView(request):
    students = studentModel.objects.all().values()
    get_student = list(students)
    return JsonResponse(get_student,safe=False)