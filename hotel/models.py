from django.db import models

# Create your models here.
class Ofice(models.Model):
	floor_ofice = models.CharField(max_length=64)
	name_ofice = models.CharField(max_length=64)
	line_ofice = models.CharField(max_length=64)