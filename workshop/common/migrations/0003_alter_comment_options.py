# Generated by Django 4.2.1 on 2023-07-06 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_like_to_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_time_of_publication']},
        ),
    ]