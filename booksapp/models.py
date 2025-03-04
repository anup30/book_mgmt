from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True, max_length=1000)
	published_year = models.IntegerField(blank=True, null=True)
	#isbn = models.CharField(max_length=15, unique=True)	

	def __str__(self):
		return self.title


