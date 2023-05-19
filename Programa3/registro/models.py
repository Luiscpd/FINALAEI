from django.db import models

# Create your models here.


class DatosUsuario(models.Model):
    DPI = models.BigIntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    email = models.EmailField(null=True, max_length=100)
    date = models.DateField(null=True)


    def __str__(self):
        return str(self.DPI)