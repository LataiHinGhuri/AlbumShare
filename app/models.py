import datetime
from django.db import models

class Album(models.Model):

	album_title = models.CharField(max_length=250)
	album_message = models.CharField(max_length=1000)
	password = models.CharField(max_length=10)
	owner = models.CharField(max_length=100, default="Mamun")
	post_date = models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.album_title

class Photo(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	images = models.CharField(max_length=250)
	counter = models.IntegerField(default=0)
	height = models.IntegerField(default=250)
	width = models.IntegerField(default=250)

class Comments(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	user = models.CharField(max_length=50)
	comment = models.CharField(max_length=100)
	def __str__(self):
		return self.user

class LoginControl(models.Model):
	logtext = models.CharField(max_length=50, default='login')
	profile = models.CharField(max_length=50, default='My Profile')
		
		