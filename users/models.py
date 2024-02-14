from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=1000)

class IMUser(AbstractUser):      
    USER_TYPE = (
        ("EIT", "EIT"),
        ("TEACHING_FELLOW", "Teaching Fellow"),
        ("ADMIN_STAFF", "Administrative Staff"),
        ("ADMIN", "Administrator")
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"{self.name} ({self.year})"


class Cohort(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateTimeField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)


class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohort_member_author')