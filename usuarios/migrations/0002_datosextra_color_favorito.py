# Generated by Django 5.0.6 on 2024-07-03 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='color_favorito',
            field=models.CharField(default='no tengo', max_length=20),
        ),
    ]
