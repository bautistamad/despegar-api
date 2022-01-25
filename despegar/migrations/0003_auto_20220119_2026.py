# Generated by Django 3.2.9 on 2022-01-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despegar', '0002_auto_20220119_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_type',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Sale', 'Sale')], default='Normal', max_length=10),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_type',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Sale', 'Sale')], default='Normal', max_length=10),
        ),
    ]