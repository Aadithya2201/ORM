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