from django.db import models

# Create your models here.

class CompanySector(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)
