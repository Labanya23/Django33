from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharFiels(max.length=100)
    price=models.FloatField(default=0.00)
    descriotion=models.CharField(max_length=100,default='abc')

    def__str__(self):
        return self.name
