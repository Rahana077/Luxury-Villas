from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    cat_name=models.CharField(max_length=100,null=True,blank=True)
    categoryImage=models.ImageField(upload_to="cimage",null=True)
    cat_description=models.CharField(max_length=100,null=True,blank=True)
    Location=models.CharField(max_length=100,null=True,blank=True)

class ProductDb(models.Model):

    c_name=models.CharField(max_length=100,null=True,blank=True)
    Pro_name=models.CharField(max_length=100,null=True,blank=True)
    ProductImage=models.ImageField(upload_to="image",null=True)
    Price=models.IntegerField(null=True,blank=True)
    ProDescription=models.CharField(max_length=100,null=True,blank=True)

class AgentsDb(models.Model):
    Agent_name=models.CharField(max_length=100,null=True,blank=True)
    Agent_id=models.IntegerField(null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)

class ContactDb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)

class feedbackDb(models.Model):

    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)








