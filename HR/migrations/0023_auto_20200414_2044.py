# Generated by Django 3.0.5 on 2020-04-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0022_addwork'),
    ]

    operations = [
        migrations.AddField(
            model_name='addwork',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='addwork',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
