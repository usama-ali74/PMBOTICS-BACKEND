# Generated by Django 4.1.5 on 2023-01-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_project_no_of_group_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
    ]