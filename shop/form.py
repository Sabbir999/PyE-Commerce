"""
This script defines a custom user registration form (`CustomUserForm`) based on Django's UserCreationForm.

Components:
- from pyexpat import model: Imports the model module from pyexpat (not directly used in the provided code).
- from django.contrib.auth.forms import UserCreationForm: Imports the UserCreationForm from Django for user registration.
- from .models import User: Imports the User model from the current package (assuming User is a custom model).

CustomUserForm Class:
- Inherits from UserCreationForm: Extends the built-in UserCreationForm to customize form fields.
- Defines form fields (`username`, `email`, `password1`, `password2`) with specific widget attributes (e.g., class, placeholder).
  - username: CharField for username input.
  - email: CharField for email address input.
  - password1: CharField for password input (first).
  - password2: CharField for password input (second, confirmation).
- Meta class:
  - Specifies the model (`User`) associated with the form.
  - Defines the fields to include in the form (username, email, password1, password2).

Usage:
- This form simplifies user registration by providing custom styling (CSS classes) and placeholders for form fields.
- It extends the functionality of Django's UserCreationForm to match specific requirements for user registration.
- To use this form, instantiate it in a Django view and render it in a template for user registration purposes.

Note:
- Ensure that the `User` model imported from `.models` represents the custom user model in your Django project.
- Customize the form further as needed based on project requirements (e.g., additional validation, error handling).
"""

from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
 
class CustomUserForm(UserCreationForm):
  username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
  email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
  password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
  class Meta:
    model=User
    fields=['username','email','password1','password2']