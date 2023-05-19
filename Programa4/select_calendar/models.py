from django.db import models

# Create your models here.

class Mes(models.Model):
    ID_dia = models.IntegerField(default=0, primary_key =True)
    dia = models.CharField(max_length=50)

    def __str__(self):
        return str(self.ID_dia) + '-' + self.dia 

class Semana(models.Model):
    ID_mes = models.IntegerField(default=0, primary_key =True)
    mes = models.CharField(max_length=50)

    def __str__(self):
        return str(self.ID_mes) + '-' + self.mes 