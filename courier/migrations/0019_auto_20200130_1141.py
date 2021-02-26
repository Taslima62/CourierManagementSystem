# Generated by Django 2.1.5 on 2020-01-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0018_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Permitted_Employee', 'Permitted_Employee'), ('Customer', 'Customer'), ('Admin', 'Admin')], max_length=20),
        ),
    ]