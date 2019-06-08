from rest_framework import generics
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer

# Create your views here.

"""
Provides a get method handler
"""
class ListTeacherView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ListStudentView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer