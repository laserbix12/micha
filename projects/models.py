
# Create your models here.
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    Descripcion = models.TextField()
    Tecnologias = models.CharField(max_length=200)
    f_creacion = models.DateTimeField(auto_now_add=True)