from distutils.command import upload
from email import message
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.cat_name
    
class Product(models.Model):
    cat_id = models.ForeignKey(Category,on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)
    price = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to = 'product',blank=True,null=True)
    description = RichTextField()
    
    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'about',blank=True,null=True)
    description = RichTextField()
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    
    def __str__(self):
        return self.email
    

   

    
