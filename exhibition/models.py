from django.db import models

class Meta:
	db_table = 'exhibition'
	
# Create your models here.
class Artist(models.Model):
	id = models.AutoField(primary_key = True)
	first_name = models.CharField(max_length = 120)
	last_name = models.CharField(max_length = 120)
	birthYear = models.IntegerField(default = 1900)
	
	def __unicode__(self):
		return self.first_name + " " + self.last_name
				
	def __str__(self):
		return self.first_name + " " + self.last_name	
		
class Painting(models.Model):
	title = models.CharField(max_length = 120)
	year = models.IntegerField(default = 1900)
	image = models.CharField(default = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Tizian_041.jpg/1024px-Tizian_041.jpg', max_length = 1000)
	author = models.ForeignKey('Artist', null = True, blank = 'True')
	
	genre = (
		('i', 'impressionism'),
		('p', 'post-impressionism'),
		('s', 'surrealism')
	)
	genre = models.CharField(max_length = 50, choices = genre, default = 'i')

	def __unicode__(self):
		return self.title
			
	def __str__(self):
		return self.title

	