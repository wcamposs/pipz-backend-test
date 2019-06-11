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
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=60)

    def create(self, validated_data):
        """
        Create and return a new 'Teacher' instance
        """
        return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Teacher' instance
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class StudentSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=60)
    teacher = TeacherSerializer(many=False)

    def create(self, validated_data):
        """
        Create and return a new 'Student' instance
        """
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Student' instance
        """
        instance.name = validated_data.get('name', instance.name)
        instance.teacher = validated_data.get('teacher', instance.teacher)
        instance.save()
        return instance