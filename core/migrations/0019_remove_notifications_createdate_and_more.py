# Generated by Django 4.1.5 on 2023-03-26 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_notifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='createdate',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='createtime',
        ),
    ]