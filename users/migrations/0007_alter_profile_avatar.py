# Generated by Django 3.2 on 2021-12-03 21:42

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20211125_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True),
        ),
    ]
