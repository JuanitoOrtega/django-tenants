from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Tenant(TenantMixin):
    name = models.CharField(max_length=100, verbose_name='Nombre del cliente')
    paid_until = models.DateField(verbose_name='Pagado hasta')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    # Auto create schema
    auto_create_schema = True
    auto_drop_schema = True
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass

    class Meta:
        verbose_name = 'Dominio'
        verbose_name_plural = 'Dominios'