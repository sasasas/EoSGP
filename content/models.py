from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class FlatPageManager(models.Manager):
	def get_page_or_blank(self, **kwargs):
		try:
			return self.get(**kwargs)
		except ObjectDoesNotExist:
			# Construct blank page
			permalink = kwargs.get('permalink', None)
			title = kwargs.get('title', permalink)
			content = ''' This page does not exist.'''
			return FlatPage(permalink = permalink, title = title, content=content)

class FlatPage(models.Model):
	permalink = models.CharField(max_length=100, unique=True)
	template_file = models.CharField(max_length=100, default='flat_page.html')
	title = models.CharField(max_length=100, blank=True)
	objects = FlatPageManager()
	subtitle = models.CharField(max_length=100, null=True, blank=True)
	content = models.TextField()

	def __unicode__(self):
		return self.permalink

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
	

