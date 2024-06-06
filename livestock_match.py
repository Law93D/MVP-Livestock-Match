# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add custom fields if needed
    pass

# matching/models.py
from django.db import models

class Livestock(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    # Add more fields as needed

# matching/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Livestock

def livestock_list(request):
    # Retrieve all livestock objects from the database
    livestock = Livestock.objects.all()
    # Convert livestock data into JSON format
    data = [{'name': animal.name, 'breed': animal.breed, 'age': animal.age} for animal in livestock]
    # Return JSON response containing livestock data
    return JsonResponse(data, safe=False)

# users/views.py
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def user_login(request):
    if request.method == 'POST':
        # Retrieve username and password from request POST data
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate user with provided credentials
        user = authenticate(request, username=username, password=password)
        # If authentication is successful, log in the user
        if user is not None:
            login(request, user)
            # Return success message as JSON response
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            # Return error message for invalid credentials as JSON response
            return JsonResponse({'message': 'Invalid credentials'}, status=400)
