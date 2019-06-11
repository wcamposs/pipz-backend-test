from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=60)
    teacher = models.ForeignKey(Teacher, related_name='students', on_delete=models.CASCADE)

    class Meta:
        ordering = ['teacher']

    def __str__(self):
        return self.name