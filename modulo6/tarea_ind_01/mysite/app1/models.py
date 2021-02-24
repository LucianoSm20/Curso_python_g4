from django.db import models

# Create your models here.

class Departamento(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre= models.CharField(max_length=255)
    descripcion= models.CharField(max_length=255)