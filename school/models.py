from django.db import models

# Create your models here.
class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    teacher = models.ForeignKey(Teacher, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name