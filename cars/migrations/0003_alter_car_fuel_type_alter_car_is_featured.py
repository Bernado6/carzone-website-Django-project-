# Generated by Django 4.0.6 on 2022-07-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_doors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
