# Generated by Django 3.0.5 on 2020-04-15 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0024_addworkstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='addworkstatus',
            name='addwork',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HR.AddWork'),
        ),
    ]
