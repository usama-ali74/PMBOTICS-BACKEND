# Generated by Django 4.1.5 on 2023-06-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_alter_user_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='fyppanel',
            name='var',
            field=models.CharField(choices=[('varified', 'varified'), ('unvarified', 'unvarified')], max_length=20, null=True),
        ),
    ]
