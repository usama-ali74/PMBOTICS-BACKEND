# Generated by Django 4.1.5 on 2023-04-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_teammember_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='milestone',
            field=models.ManyToManyField(default=3, to='core.milestone'),
        ),
    ]
