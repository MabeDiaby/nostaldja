# Generated by Django 4.0.1 on 2022-01-12 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decades',
            name='start_year',
            field=models.CharField(max_length=100),
        ),
    ]