# Generated by Django 5.1 on 2024-09-13 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_tenant_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domain',
            options={'verbose_name': 'Dominio', 'verbose_name_plural': 'Dominios'},
        ),
    ]