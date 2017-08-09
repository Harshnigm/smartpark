from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
	A1=models.CharField(max_length=200)
	A2=models.CharField(max_length=200)
	A3=models.CharField(max_length=200)
	A4=models.CharField(max_length=200)

   



	def __unicode__(self):
		return str(self.timestamp)
	def __str__(self):
		return str(self.timestamp)

