# Generated by Django 4.0.1 on 2022-05-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main1', '0004_alter_myuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
