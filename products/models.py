from django.db import models
from categories.models import Category

class Product(models.Model):
  product_name = models.CharField(max_length=100, unique=True)
  product_description = models.TextField(max_length=300)
  product_price = models.DecimalField(max_digits=6, decimal_places=2)
  product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
  product_image = models.ImageField(upload_to='products/')

  def __str__(self):
    return self.product_name