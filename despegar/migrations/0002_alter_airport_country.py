# Generated by Django 3.2.9 on 2021-11-08 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('despegar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pais', to='despegar.country'),
        ),
    ]