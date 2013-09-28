from django.db import models

class Tweet(models.Model):
   text=models.CharField(max_length=140)
   sender=models.CharField(max_length=50)
   latitude=models.DecimalField(max_digits=11,decimal_places=8,null=True)
   longitude=models.DecimalField(max_digits=11,decimal_places=8,null=True)
   keywords=models.ManyToManyField('Keyword')
   date=models.DateTimeField(auto_now_add=True,null=True)

class Text(models.Model):
   text=models.CharField(max_length=400)
   sender=models.CharField(max_length=10)
   latitude=models.DecimalField(max_digits=11,decimal_places=8,null=True)
   longitude=models.DecimalField(max_digits=11,decimal_places=8,null=True)
   keywords=models.ManyToManyField('Keyword')
   date=models.DateTimeField(auto_now_add=True,null=True)

class Keyword(models.Model):
   word=models.CharField(max_length=100)
