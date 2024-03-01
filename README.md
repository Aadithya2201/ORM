# Ex02 Django ORM Web Application
## Date: 29.02.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![alt text](<Screenshot (2).png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py
from django.db import models
from django.contrib import admin
class books(models.Model):  
	book_name=models.CharField(max_length=50);
	author=models.CharField(max_length=50);
	book_no=models.IntegerField(primary_key=True);
	book_price=models.IntegerField()
	quantity=models.IntegerField()
class booksAdmin(admin.ModelAdmin):
	list_display=( "book_name","author","book_no","book_price","quantity");

admin.py
from django.contrib import admin
from .models import books,booksAdmin
admin.site.register(books,booksAdmin)
```

## OUTPUT

![alt text](<Screenshot (3).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
