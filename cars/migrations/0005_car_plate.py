# Generated by Django 5.0.3 on 2024-03-28 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
