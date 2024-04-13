from django.db import models

class Plant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    room = models.CharField(max_length=20)
    last_time_watered = models.DateTimeField(null = True, blank=True)

