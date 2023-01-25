from django.db import models

# Create your models here.
class Food(models.Model):
	name = models.TextField()
	carbs = models.TextField()
	saturated_fat = models.TextField()

	