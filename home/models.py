from django.db import models

# Create your models here.
class Igdatabse(models.Model):
      file = models.FileField(upload_to='files/')