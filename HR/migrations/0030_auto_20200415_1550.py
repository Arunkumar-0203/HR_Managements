# Generated by Django 3.0.5 on 2020-04-15 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0029_attreport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attreport',
            old_name='date',
            new_name='absent',
        ),
        migrations.RenameField(
            model_name='attreport',
            old_name='description',
            new_name='present',
        ),
    ]
