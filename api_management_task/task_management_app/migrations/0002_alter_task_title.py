# Generated by Django 5.1.2 on 2024-10-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
