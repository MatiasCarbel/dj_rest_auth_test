from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    document_number = models.CharField(max_length=8)
    birth_date = models.DateField(null=True)
    province = models.CharField(max_length=25)
    city = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.user} -Patient_ID:{self.id}'