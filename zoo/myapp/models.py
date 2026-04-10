from django.db import models


class Enclosures(models.Model):
    description = models.CharField(max_length=200)
    size = models.IntegerField()
    
    def __str__(self):
        return self.description


class Animals(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    health = models.CharField(max_length=100)
    enclosure_id = models.ForeignKey(Enclosures, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
