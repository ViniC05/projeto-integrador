# Generated by Django 4.2.1 on 2023-06-02 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_portal_bairro_portal_rua'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portal',
            name='days',
            field=models.IntegerField(default=0),
        ),
    ]
