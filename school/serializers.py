from rest_framework import serializers
from rest_framework import exceptions

from django.contrib.auth import authenticate

from .models import Student, Teacher


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)

        else:
            msg = "Must provide username and password both"
            raise exceptions.ValidationError(msg)
        return data


class TeacherSerializer(serializers.Serializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name')


class StudentSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False, read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'name', 'teacher')