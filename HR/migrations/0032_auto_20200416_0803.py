# Generated by Django 3.0.5 on 2020-04-16 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0031_auto_20200415_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attreport',
            name='attendance',
        ),
        migrations.AddField(
            model_name='attreport',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HR.Employee'),
        ),
    ]
