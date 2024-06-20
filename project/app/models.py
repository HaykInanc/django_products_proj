from django.db import models

# Create your models here.


# add new model Task with fields: title, done_flg
# make migrations and add 3 task

class Task(models.Model):
    title = models.CharField(max_length=120)
    done_flg = models.BooleanField()

    def __str__(self):
        return self.title 
    

class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.IntegerField()

    def __str__(self):
        return self.title 
    