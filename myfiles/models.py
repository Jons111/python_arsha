from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    deadline = models.DateField()
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    description = models.TextField()
    picture1 = models.ImageField(upload_to='media')
    picture2 = models.ImageField(upload_to='media',null=True,blank=True)
    picture3 = models.ImageField(upload_to='media',null=True,blank=True)
    date = models.DateTimeField(auto_now=True)

