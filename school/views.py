from django.contrib.auth import login as django_login, logout as django_logout
#from django.http import Http404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
#from rest_framework import status

from .models import Student, Teacher
from .serializers import StudentSerializer, StudentResponseSerializer, TeacherSerializer, LoginSerializer

# Create your views here.

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)


class ListTeacherView(generics.ListCreateAPIView):
    """
    List all teachers, or create a new teacher 
    """

    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ListStudentView(generics.ListCreateAPIView):
    """
    List all students, or create a new student
    """

    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)

    queryset = Student.objects.all()
    serializer_class = StudentResponseSerializer

    def create(self, *args, **kwargs):
        self.serializer_class = StudentSerializer
        return generics.ListCreateAPIView.create(self, *args, **kwargs)

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a 'Teacher' instance
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a 'Student' instance
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def retrieve(self, *args, **kwargs):
        self.serializer_class = StudentResponseSerializer
        return generics.RetrieveUpdateDestroyAPIView.retrieve(self, *args, **kwargs)
