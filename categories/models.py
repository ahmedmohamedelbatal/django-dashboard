from django.db import models

class Category(models.Model):
  category_name = models.CharField(max_length=100, unique=True)
  category_description = models.TextField(max_length=300)
  category_image = models.ImageField(upload_to='categories/')
  
  class Meta:
    verbose_name = ("Category")
    verbose_name_plural = ("Categories")
    
  def __str__(self):
    return self.category_name