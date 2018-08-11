from django.db import models
from django.conf import settings
import datetime
# Create your models here.

class author(models.Model):
	name = models.CharField(max_length=30)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
	submitedon = models.DateField(default=datetime.date.today)
	isapproved = models.BooleanField(default=False)
	isdeleted = models.BooleanField(default=False)


class category(models.Model):
	name = models.CharField(max_length=30)
	submitedon = models.DateField(default=datetime.date.today)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
	isapproved = models.BooleanField(default=False)
	isdeleted = models.BooleanField(default=False)
	

class quotes(models.Model):
	quotes = models.CharField(max_length=500)
	author = models.ForeignKey(author, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
	submitedon = models.DateField(default=datetime.date.today)
	category = models.ForeignKey(category, on_delete=models.CASCADE)
	shareFacebook = models.IntegerField(default=0)
	shareWhatsapp = models.IntegerField(default=0)
	shareInstagram = models.IntegerField(default=0)
	copyquotes = models.IntegerField(default=0)
	isapproved = models.BooleanField(default=False)
	isdeleted = models.BooleanField(default=False)


	


