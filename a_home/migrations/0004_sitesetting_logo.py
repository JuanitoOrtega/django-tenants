# Generated by Django 5.1 on 2024-09-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_home', '0003_sitesetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/', verbose_name='Logo'),
        ),
    ]
