# Generated by Django 4.2.1 on 2023-07-11 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='profile_picture',
            field=models.URLField(default='/static/images/person.png'),
        ),
    ]