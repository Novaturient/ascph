# Generated by Django 2.1.8 on 2019-05-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monnit', '0006_sensordata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='Battery',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='SignalStrength',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='State',
            field=models.IntegerField(),
        ),
    ]
