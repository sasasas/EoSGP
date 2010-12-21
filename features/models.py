from django.db import models

class Event(models.Model):
	datetime = models.DateTimeField()
	name = models.CharField(max_length=100)
	venue = models.CharField(max_length=100)
	detail = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['datetime']

class Author(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)

	def fullname(self):
		return self.firstname+" "+self.lastname
	def __unicode__(self):
		return self.fullname()

class BookOfTheMonth(models.Model):
	date = models.DateField()
	title = models.CharField(max_length=100)
	author = models.ManyToManyField(Author)
	publisher = models.CharField(max_length=30)
	reviewer = models.CharField(max_length=30)
	review = models.TextField()
	detail = models.TextField(blank=True)

	def __unicode__(self):
		return self.title


