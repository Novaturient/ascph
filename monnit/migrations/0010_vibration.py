# Generated by Django 2.1.8 on 2019-06-03 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monnit', '0009_auto_20190530_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vibration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRead', models.CharField(max_length=255, unique=True)),
                ('reading', models.CharField(max_length=255)),
            ],
        ),
    ]
