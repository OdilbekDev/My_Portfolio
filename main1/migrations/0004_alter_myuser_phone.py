# Generated by Django 4.0.1 on 2022-05-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main1', '0003_alter_myuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
