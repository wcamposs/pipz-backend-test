from django.urls import path
from .views import ListStudentView, ListTeacherView

urlpatterns = [
    path('students/', ListStudentView.as_view(), name="students-all"),
    path('teachers/', ListTeacherView.as_view(), name="teachers-all"),
]