from django.db import models

class About(models.Model):
	paragraph_number = models.IntegerField()
	subtitle = models.CharField(max_length=100, null=True)
	content = models.TextField()

	def __unicode__(self):
		return self.paragraph_number

	class Meta:
		ordering = ['paragraph_number']

class DoctrinalStatement(models.Model):
	paragraph_number = models.IntegerField()
	subtitle = models.CharField(max_length=100, null=True)
	content = models.TextField()

	def __unicode__(self):
		return self.paragraph_number

	class Meta:
		ordering = ['paragraph_number']

class Apprenticeship(models.Model):
	paragraph_number = models.IntegerField()
	subtitle = models.CharField(max_length=100, null=True)
	content = models.TextField()

	def __unicode__(self):
		return self.paragraph_number

	class Meta:
		ordering = ['paragraph_number']

class LinksBlurb(models.Model):
	paragraph_number = models.IntegerField()
	subtitle = models.CharField(max_length=100, null=True)
	content = models.TextField()

	def __unicode__(self):
		return self.paragraph_number

	class Meta:
		ordering = ['paragraph_number']

class Link(models.Model):
	list_position_number = models.IntegerField()
	name = models.CharField(max_length=200)
	url = models.URLField(verify_exists=False)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['list_position_number']

class PartnersBlurb(models.Model):
	paragraph_number = models.IntegerField()
	subtitle = models.CharField(max_length=100, null=True)
	content = models.TextField()

	def __unicode__(self):
		return self.paragraph_number

	class Meta:
		ordering = ['paragraph_number']

class Partner(models.Model):
	name = models.CharField(max_length=100)
	address = models.TextField(null=True)
	town = models.CharField(max_length=25, null=True)
	postcode = models.CharField(max_length=10, null=True)
	telephone = models.CharField(max_length=15, null=True)
	email = models.EmailField(null=True)
	
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
	

