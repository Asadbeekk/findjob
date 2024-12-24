from datetime import datetime

from django.db import models


class SignUp(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class SignIn(models.Model):
    objects = None
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.email}"


class AddJob(models.Model):
    EMPLOYMENT_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def upload_path(instance, filename):
    return datetime.today().strftime("%Y/%m/%d/{filename}")