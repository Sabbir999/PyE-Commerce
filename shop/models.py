"""
Django Models for Online Shopping Application:

Catagory Model:
- Represents a product category with fields for name, image, description, status, and creation timestamp.
- Uses an ImageField for storing category images, with a custom upload path function (`getFileName`).
- Provides a string representation (`__str__`) for the category name.

Product Model:
- Represents a product with fields related to its category, name, vendor, image, quantity, prices, description, status, trending status, and creation timestamp.
- Utilizes ForeignKey to link to the Category model.
- Includes ImageField for storing product images, with a custom upload path function (`getFileName`).
- Defines a string representation (`__str__`) for the product name.

Cart Model:
- Represents a user's cart item with fields for the user, associated product, quantity, and creation timestamp.
- Uses ForeignKey to link to the User and Product models.
- Includes a property (`total_cost`) to calculate the total cost of items in the cart.

Favourite Model:
- Represents a user's favorite product with fields for the user, associated product, and creation timestamp.
- Uses ForeignKey to link to the User and Product models.

Functionality:
- The `getFileName` function generates a unique filename for uploaded images based on the current timestamp.
- Django models define relationships (ForeignKey) between entities and include field types for various data types (CharField, ImageField, IntegerField, FloatField, TextField, BooleanField, DateTimeField).
- Custom string representations (`__str__`) are provided for each model to improve readability in Django admin and other contexts.

Usage:
- Integrate these models into a Django project to manage product categories, products, user carts, and favorites.
- Configure Django admin to interact with and manage these models via the Django admin interface.
- Customize model fields and behaviors as needed based on specific project requirements.


"""

from itertools import product
from django.db import models
from django.contrib.auth.models import User
import datetime
import os
 
def getFileName(requset,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)
 
class Catagory(models.Model):
  name=models.CharField(max_length=150,null=False,blank=False)
  image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    return self.name
 
class Product(models.Model):
  category=models.ForeignKey(Catagory,on_delete=models.CASCADE)
  name=models.CharField(max_length=150,null=False,blank=False)
  vendor=models.CharField(max_length=150,null=False,blank=False)
  product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
  quantity=models.IntegerField(null=False,blank=False)
  original_price=models.FloatField(null=True,blank=True)
  selling_price=models.FloatField(null=False,blank=False)
  description=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    return self.name
class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(Product,on_delete=models.CASCADE)
  product_qty=models.IntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)
 
  @property
  def total_cost(self):
    return self.product_qty*self.product.selling_price
 
class Favourite(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
 