from django.db import models
import datetime
from django.utils.timezone import now





# Create your models here.

class BreakFast(models.Model):

    title = models.CharField(max_length = 100 , blank =True , null = True)
    price = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = '')
    desc  = models.TextField( blank = True , null = True )

    def __str__(self):
        return self.title

class Lunch(models.Model):

    title = models.CharField(max_length = 100 , blank =True , null = True)
    price = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = 'lunch')
    desc  = models.TextField( blank = True , null = True )

    def __str__(self):
        return self.title


class Dinner(models.Model):

    title = models.CharField(max_length = 100 , blank =True , null = True)
    price = models.IntegerField(default = 0)
    image = models.ImageField(upload_to = 'lunch')
    desc  = models.TextField( blank = True , null = True )

    def __str__(self):
        return self.title

City_Name = (
('Alexandria' , 'Alexandria'),
('Cairo' , 'Cairo'),
('Portsaid' , 'Portsaid'),
('Giza' , 'Giza'),
('Aswan' , 'Aswan')
)

class Orders(models.Model):
    order_name        = models.ForeignKey(BreakFast , related_name = 'apply_order' , on_delete = models.CASCADE , null = True , blank = True)
    order_name_lunch  = models.ForeignKey(Lunch, related_name = 'apply_order_lunch' , on_delete = models.CASCADE , null = True , blank = True)
    order_name_dinner = models.ForeignKey(Dinner, related_name = 'apply_order_dinner' , on_delete = models.CASCADE , null = True , blank = True)
    name              = models.CharField(max_length = 50)
    address           = models.CharField(max_length = 250)
    city              = models.CharField(max_length = 25 , choices= City_Name)
    phone             = models.IntegerField()
    ordered_at        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ordered_at)
