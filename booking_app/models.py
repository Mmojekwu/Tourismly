from django.db import models

# Create your models here.

class Person(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    comments = models.CharField(max_length=1000, default='DEFAULT VALUE', blank=True, null=True)
    
    def __str__(self):
        return self.user_name
    