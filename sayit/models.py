from django.db import models


class Example(models.Model):
	title = models.CharField(max_length=80)
	product_type = models.CharField(max_length=100)
	review = models.TextField(max_length=500, unique=True)
	order = models.IntegerField(default=0)
	STATUS_CHOICES = (
		('d', 'Draft'),
		('p', 'Published'),
	)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES,
							  default='d')

	class Meta:
		ordering = ["order"]

	def __str__(self):
		return self.title


class Musician(models.Model):
	name = models.CharField(max_length=80, unique=True)
	position = models.CharField(max_length=100)
	musical_styles = models.CharField(max_length=100)
	image = models.ImageField(blank=True, null=True, upload_to='musicians/')
	bio = models.TextField(max_length=500, unique=True)
	profile_url = models.URLField(max_length=100)
	order = models.IntegerField(default=0)
	STATUS_CHOICES = (
		('d', 'Draft'),
		('p', 'Published'),
	)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES,
							  default='d')

	class Meta:
		ordering = ["order"]

	def __str__(self):
		return self.name
