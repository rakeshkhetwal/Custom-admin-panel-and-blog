from django.db import models
from django.urls import reverse

# Create your models here.

class banner(models.Model):

    authorized=models.ForeignKey('auth.User',null=True)
    type=models.IntegerField()
    photo = models.FileField(upload_to='documents/')
    heading = models.CharField(max_length=250,null=True)
    description = models.TextField(null=True)
    openings = models.IntegerField(null=True)
    name = models.CharField(max_length=250,null=True)
    linkfb = models.URLField(null=True)
    linkinsta = models.URLField(null=True)
    linklin = models.URLField(null=True)
    designation= models.CharField(max_length=100,null=True)


