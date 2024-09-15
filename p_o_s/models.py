from django.db import models

# Create your models here.
    
class User(models.Model):
    username = models.CharField(max_length = 50)
    email = models.TextField()
    password = models.TextField()
    userId = models.CharField(max_length = 10)
    role = models.TextField()
    name = models.TextField()
    
class Permission(models.Model):
    name = models.CharField(max_length = 10)
    permissionId = models.CharField(max_length = 10)

class Role(models.Model):
    name = models.CharField(max_length = 10)
    roleId = models.CharField(max_length = 10)
    permissionId = models.ForeignKey(Permission,on_delete=models.CASCADE)
    
class Category(models.Model):
    title = models.CharField(max_length=50)
    CategoryId = models.CharField(max_length=10)

class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField()
    price = models.BigIntegerField()
    image = models.ImageField(upload_to ='pictures')
    User = models.CharField(max_length = 50)
    Contact = models.TextField()
    
    
class Payment(models.Model):
    paymentId = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    
class Customer(models.Model):
    name = models.CharField(max_length=50)
    customerId = models.CharField(max_length=10)
    
class Sales(models.Model):
    date = models.DateField()
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product,on_delete=models.CASCADE)
    paymentId= models.ForeignKey(Payment,on_delete=models.CASCADE)
    customerId= models.ForeignKey(Customer,on_delete=models.CASCADE)  
       
class Reward(models.Model):
    points =models.IntegerField()
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)     

