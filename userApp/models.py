from django.db import models

# Create your models here.
class UserRegistrationDb(models.Model):
        uname = models.CharField(max_length=50, null=True, blank=True)
        uemail = models.EmailField(max_length=50, null=True, blank=True)
        upass = models.CharField(max_length=50, null=True, blank=True)
        umob = models.IntegerField(null=True, blank=True)
        uimg = models.ImageField(upload_to='profile pic', null=True, blank=True)
class bookslot(models.Model):
        fname=models.CharField(max_length=50,null=True,blank=True)
        lname=models.CharField(max_length=50,null=True,blank=True)
        email=models.EmailField(max_length=50,null=True,blank=True)
        token=models.CharField(max_length=50,null=True,blank=True)

class payment(models.Model):
        cardnum=models.CharField(max_length=50,null=True,blank=True)
        name=models.CharField(max_length=50,null=True,blank=True)
        cardnumber=models.CharField(max_length=50,null=True,blank=True)
        expire=models.CharField(max_length=50,null=True,blank=True)
        cvv=models.CharField(max_length=50,null=True,blank=True)