# Generated by Django 4.2.1 on 2023-05-21 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
