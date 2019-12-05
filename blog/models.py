from django.db import models

# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=100)
	text=models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	slug=models.SlugField(max_length=100)
	image=models.ImageField(upload_to='post_images')
