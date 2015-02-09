from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
	name = models.CharField(max_length=150)
	slug = models.SlugField(unique=True)
	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super(Category,self).save(*args,**kwargs)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = 'categories'

class Post(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=300)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True, default='2010-10-10 10:10:10')
	modified = models.DateTimeField(auto_now=True, default='2010-10-10 10:10:10')

	featured_image = models.ImageField(upload_to='uploads', blank=True)
	def __str__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length=150)
	post = models.ManyToManyField(Post)