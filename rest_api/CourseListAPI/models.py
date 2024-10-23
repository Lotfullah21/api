from django.db import models

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title  = models.CharField(max_length=120)   
    def __str__(self):
        return self.title
    
class Course(models.Model):
    title = models.CharField(max_length=120)
    instructor = models.CharField(max_length=120)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)