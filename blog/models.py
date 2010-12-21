from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	datetime = models.DateTimeField()
	user = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	content = models.TextField()

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-datetime']




