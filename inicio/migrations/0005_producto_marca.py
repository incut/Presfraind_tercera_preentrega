# Generated by Django 5.0.6 on 2024-07-01 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_producto_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.CharField(default='proyecto', max_length=20),
        ),
    ]
