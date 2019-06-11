from django.urls import path
from .views import ListStudentView, ListTeacherView, LoginView, LogoutView, StudentDetail, TeacherDetail

urlpatterns = [
    path('students/', ListStudentView.as_view(), name="students-list"),
    path('teachers/', ListTeacherView.as_view(), name="teachers-list"),
    path('teachers/<int:pk>/', TeacherDetail.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]