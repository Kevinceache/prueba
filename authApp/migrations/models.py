from django.db import models

class Entidad(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_lenght=30)
    
