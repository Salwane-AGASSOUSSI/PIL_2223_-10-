# Generated by Django 3.2.19 on 2023-06-30 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0007_alter_adminuser_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminuser',
            name='a_email',
        ),
    ]
