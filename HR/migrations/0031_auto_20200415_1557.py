# Generated by Django 3.0.5 on 2020-04-15 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0030_auto_20200415_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attreport',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='attreport',
            name='hr',
        ),
    ]
