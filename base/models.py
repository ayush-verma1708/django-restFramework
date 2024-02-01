from django.db import models

# Create your models here.
class drinks(models.Model):
    name = models.CharField(max_length = 255,blank = False)
    price = models.IntegerField(blank = False)

    def __str__(self):
        return self.name