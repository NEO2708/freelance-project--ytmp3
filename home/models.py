from django.db import models

# Create your models here.
class Igdatabse(models.Model):
    id=models.AutoField
    img=models.FileField(upload_to="post/",max_length=300,null=True,default=None)