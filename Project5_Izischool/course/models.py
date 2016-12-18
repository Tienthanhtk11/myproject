from django.db import models


# Create your models here.
class course(models.Model):
    id = models.AutoField("Id", primary_key=True)
    name = models.CharField("Name", max_length=256)
    subtitle = models.CharField("Subtitle", max_length=256)
    image=models.CharField("Image",max_length=256)
    price = models.FloatField("Price")
    hitcount = models.IntegerField("HitCount")
