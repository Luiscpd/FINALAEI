from django.db import models

# Create your models here.
class Puntos(models.Model):
    ID_coordenadas = models.AutoField(primary_key =True)
    x1 = models.IntegerField(default=0)
    y1 = models.IntegerField(default=0)
    x2 = models.IntegerField(default=0)
    y2 = models.IntegerField(default=0)

    def __str__(self):
        return '('+ str(self.x1) + ',' + str(self.x2) + ')' + ' - ' + '(' + str(self.x2) + ',' + str(self.y2) + ')'