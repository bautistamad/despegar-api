# Generated by Django 3.2.9 on 2022-01-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despegar', '0004_auto_20220119_2026'),
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