from re import search
from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_name']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title','slug','description','cat_id','image','price']
    search_fields = ['title','cat_id']
    
@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    list_display = ['title','description','image']
    

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['email','subject','message']
    

    
    



