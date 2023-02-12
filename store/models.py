from django.db import models
class Product(models.Model):
    
	image = models.ImageField(null=True, blank=True)

	

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url