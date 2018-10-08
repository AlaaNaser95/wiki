from django.db import models

# Create your models here.
class Page(models.Model):
	title=models.CharField(max_length=200)
	content=models.TextField()
	last_update=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return 'pages_detail/' + str(self.id)
