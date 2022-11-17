from django.db import models
import dimod
# Create your models here.
class Matrix(models.Model):
    input1 = models.IntegerChoices
    input2 = models.IntegerChoices
    input2 = models.IntegerChoices
bqm = dimod.Exact