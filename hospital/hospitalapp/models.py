from django.db import models
from PIL import Image 
from django.contrib.auth.models import User
class profilepic(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="profile_pic",default="profile_pic/default.png")
