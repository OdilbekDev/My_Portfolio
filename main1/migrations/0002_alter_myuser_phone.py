# Generated by Django 4.0.1 on 2022-05-07 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
