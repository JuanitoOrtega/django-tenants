from django.db import models
from colorfield.fields import ColorField


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name


class SiteSetting(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    color = ColorField(default='#FF0000')
    logo = models.ImageField(upload_to='logos/', null=True, blank=True, verbose_name="Logo")
    
    class Meta:
        verbose_name = "Configuración"
        verbose_name_plural = "Configuraciones"

    def __str__(self):
        return self.name