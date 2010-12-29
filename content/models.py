from django.db import models

class About(models.Model):
	subtitle = models.CharField(max_length=100)
	content = models.TextField()

	def __unicode__(self):
		return self.subtitle

	#class Meta:
	#	ordering = ['datetime']
	
