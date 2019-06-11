from django.urls import path
from .views import ListStudentView, ListTeacherView, LoginView, LogoutView

urlpatterns = [
    path('', ListStudentView.as_view(), name="students-list"),
    path('teachers/', ListTeacherView.as_view(), name="teachers-list"),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]