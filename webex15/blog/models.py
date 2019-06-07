from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Author(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	bio = models.TextField()

	class Meta:
		ordering = ["user_id","bio"]

	def __str__(self):
		return str(self.user_id)

class Post(models.Model):
	date = models.DateField(auto_now_add=True)
	title = models.CharField(max_length=100)
	text = models.TextField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	post_id = models.AutoField(primary_key=True)

	class Meta:
		ordering = ["-date"]

	def get_absolute_url(self):
		return reverse('post-detail', args=[str(self.post_id)])

	def __str__(self):
		return self.title +' (' + str(self.date) +') - ' + str(self.author)

class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	text = models.TextField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	class Meta:
		ordering = ["-date"]

	def __str__(self):
		return str(self.author) + ' (' + str(self.date) + ') - ' + self.text
