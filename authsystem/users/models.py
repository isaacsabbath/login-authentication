from django.db import models
from django.contrib.auth.models import user
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	
