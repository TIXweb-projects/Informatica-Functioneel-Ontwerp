from django.db import models
from django.conf import settings

class Hond(models.Model):
    naamHond = models.CharField(max_length=100)
    eigenaarNaam = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plaats = models.CharField(max_length=100)
    # zichtbaar_op_site = models.BooleanField(default=False)

    def __str__(self):
        return self.naamHond
    
class Uitlater(models.Model):
    naamUitlater = models.CharField(max_length=100)
    plaats = models.CharField(max_length=100)
    # gebruiker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gebruiker = models.CharField(max_length=100)
    def __str__(self):
        return self.naamUitlater