from django.db import models

class FlatPage(models.Model):
	permalink = models.Charfield(max_length=100, unique=True)
	title = models.CharField(max_length=100, blank=True)
	subtitle = models.CharField(max_length=100, null=True, blank=True)
	content = models.TextField()

	def __unicode__(self):
		return permalink

class Link(models.Model):
	list_position_number = models.IntegerField()
	name = models.CharField(max_length=200)
	url = models.URLField(verify_exists=False)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['list_position_number']

class Partner(models.Model):
	name = models.CharField(max_length=100)
	address = models.TextField(null=True, blank=True)
	town = models.CharField(max_length=25, null=True, blank=True)
	postcode = models.CharField(max_length=10, null=True, blank=True)
	telephone = models.CharField(max_length=15, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
	

