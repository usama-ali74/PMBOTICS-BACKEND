# Generated by Django 4.1.5 on 2023-01-18 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_user_designation_remove_user_facultyid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='fyppanel',
            name='facultyid',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='milestone_name',
            field=models.CharField(max_length=75, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]