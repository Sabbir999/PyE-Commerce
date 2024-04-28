"""
This script registers Django models with the Django admin interface for easy management and administration.

Functionality:
- from atexit import register: Imports the register function from the atexit module.
- from django.contrib import admin: Imports the admin module from Django for setting up the admin interface.
- from .models import *: Imports all models from the current package (assuming the models are defined in models.py).
"""

from atexit import register
from django.contrib import admin
from .models import *

"""
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'image', 'description')
admin.site.register(Catagory,CategoryAdmin)
"""
 
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)
