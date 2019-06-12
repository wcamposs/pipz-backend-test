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


class StudentResponseSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=60)
    teacher = TeacherSerializer(many=False, required=True)


class StudentSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=60)
    teacher_id = serializers.IntegerField(required=True)
        
    def create(self, validated_data):
        """
        Create and return a new 'Student' instance
        """
        student = Student.objects.create(**validated_data)
        return student

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Student' instance
        """
        instance.name = validated_data.get('name', instance.name)
        instance.teacher_id = validated_data.get('teacher_id', instance.teacher_id)
        instance.save()
        return instance