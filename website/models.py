from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager
from datetime import datetime

# class register(AbstractBaseUser):
# 	objects=UserManager()
# 	name=models.CharField(max_length=50)
# 	emailid=models.EmailField(max_length=70,blank=True, null= True)
# 	password=models.CharField(max_length=11)
# 	USERNAME_FIELD='emailid'
# 	REQUIRED_FIELDS=['password']


class register(models.Model):
	objects=UserManager()
	name=models.CharField(max_length=5000)
	emailid=models.EmailField(max_length=70)
	password=models.CharField(max_length=700)
	# USERNAME_FIELD='emailid'
	# REQUIRED_FIELDS=['password']

	def __str__(self):
		return self.name



class NewsFeed(models.Model):

	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)

class Comment(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField(max_length=100)
	website=models.CharField(max_length=200)
	comment=models.CharField(max_length=10000)
	type=models.CharField(max_length=100)
	date=models.DateTimeField(auto_now_add=True)
		
		