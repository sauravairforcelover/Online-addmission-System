from django.db import models
from django.contrib.auth.models import User

class FormData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    religion = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    eid = models.EmailField(max_length=100)
    blood_group = models.CharField(max_length=5)
    marital_status = models.CharField(max_length=10)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name
