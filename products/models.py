from django.db import models
from mptt.models import TreeForeignKey,MPTTModel


class Category(MPTTModel):
    name= models.CharField(max_length=100,unique=True)
    parent = TreeForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    class MPTTMeta:
        order_insertion_by=["name"]
    
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)   
    category = TreeForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)  
    description = models.TextField(blank=True)
    is_digital= models.BooleanField (default=False)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
       