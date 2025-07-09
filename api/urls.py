from django.urls import path
from . import views

urlpatterns = [
    # student app
    path('students/',views.studentsView,name='studentsView'),
    path('student/<int:pk>/',views.studentDetailView,name='studentDetailView'),

    # employee app
    path('employee/',views.employeeView.as_view(),name='employeeView')
]
