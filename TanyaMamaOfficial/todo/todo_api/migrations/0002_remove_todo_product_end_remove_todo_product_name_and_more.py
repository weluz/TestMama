# Generated by Django 4.2.1 on 2023-06-02 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='Product_End',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='Product_Name',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='Product_Start',
        ),
    ]