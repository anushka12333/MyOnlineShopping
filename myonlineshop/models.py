from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField( max_length=50)
    category=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image=models.ImageField(upload_to="myonlineshop/images",default="")
    def __str__(self):
       return self.product_name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField( max_length=50)
    email=models.CharField(max_length=80,default="")
    phone=models.CharField(max_length=80,default="")
    desc=models.CharField(max_length=500,default="")    
    def __str__(self):
       return self.name

       
class Order(models.Model):  
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    name =  models.CharField(max_length=100)      
    email= models.CharField(max_length=100)      
    address= models.CharField(max_length=100)      
    city= models.CharField(max_length=100)      
    state= models.CharField(max_length=50)      
    zip_code= models.CharField(max_length=50)
    phone=models.IntegerField()

    def __str__(self):
       return self.name

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
       return self.update_desc[0:7] + "..."      