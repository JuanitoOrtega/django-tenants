from django.apps import AppConfig


class ATenantManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_tenant_manager'
    
    verbose_name = "Administrador de clientes"
