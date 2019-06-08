from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer

# Create your tests here.

#Test for views
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_teacher(id="", name=""):
        if id != "" and name != "":
            Teacher.objects.create(id=id, name=name)


    def create_student(id="", name=""):
        if id != "" and name != "":
            Student.objects.create(id=id, name=name)


    def setUp(self):
        #adding test data
        self.create_teacher(1, "Matheus") 
        #self.create_student(3, "Joao")   # <--- ARRUMAR


class GetAllTest(BaseViewTest):

    """
        Ensure that all students and teachers added in the setUp method
        exist when we make an GET request to the endpoint
    """

    def test_get_all_teachers(self):
        #hit API endpoint
        response = self.client.get(reverse("teachers-all", kwargs={"version": "v1"}))

        #fetch data from sqlite
        expected = Teacher.objects.all()
        serialized = TeacherSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_all_students(self):
        #hit API endpoint
        response = self.client.get(reverse("students-all", kwargs={"version": "v1"}))

        #fetch data from sqlite
        expected = Student.objects.all()
        serialized = StudentSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)