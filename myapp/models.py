from django.db import models

# Create your models here.

class UserMaster(models.Model):
    userid=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=30)
    def __str__(self):
        return self.userid;

class UserProfile(models.Model):
    username=models.CharField(max_length=30 )
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    mob=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    # userid=models.OneToOneField(UserMaster , on_delete=models.CASCADE , primary_key=True)
    userid=models.ForeignKey(UserMaster , on_delete=models.CASCADE)
    def __str__(self):
        return str(self.userid)

class ProductCategory(models.Model):
    pcid=models.CharField(max_length=30,primary_key=True)
    pcname=models.CharField(max_length=30)
    def __str__(self):
        return self.pcid+"-"+self.pcname;
    
class Product(models.Model):
    pid=models.CharField(max_length=30,primary_key=True)
    pname=models.CharField(max_length=30)
    pdesc=models.CharField(max_length=100)
    price=models.IntegerField()
    discount=models.IntegerField()
    pcid=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    def __str__(self):
        return self.pid;

class Complaint(models.Model):
    compid=models.IntegerField(auto_created=True,primary_key=True)
    compdesc=models.CharField(max_length=500)
    compdt=models.DateField()
    status=models.CharField(max_length=10, default="open")
    userid=models.ForeignKey(UserMaster,on_delete=models.CASCADE)

    def __str__(self):
        return self.compid