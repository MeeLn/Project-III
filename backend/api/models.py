from django.db import models

FACULTY_CHOICES = [
    ('BEIT', 'BEIT'),
    ('Computer', 'Computer'),
    ('Software', 'Software'),
    ('Civil', 'Civil'),
]

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    faculty = models.CharField(max_length=20, choices=FACULTY_CHOICES)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
