# Generated by Django 3.0.5 on 2020-04-13 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0018_interview_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leavetype', models.CharField(max_length=100)),
                ('fromdate', models.CharField(max_length=100)),
                ('noday', models.CharField(max_length=100)),
                ('enddate', models.CharField(max_length=100)),
                ('leaveperiod', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.Employee')),
            ],
        ),
    ]
