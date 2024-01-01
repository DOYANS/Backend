'''
medical data models
'''

from django.db import models

class MedicalModel(models.Model):

    serialNumber = models.PositiveBigIntegerField(primary_key=True)
    title = models.CharField(max_length=150,)
    description = models.TextField()
