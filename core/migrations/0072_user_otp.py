# Generated by Django 4.1.5 on 2023-05-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0071_alter_notification_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(default=None, max_length=200),
        ),
    ]