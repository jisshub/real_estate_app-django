from django.db import models


# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=30)
    photo = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    ismvp = models.BooleanField(default=False)
    hireDate = models.DateField()

    def __str__(self):
        return self.name
