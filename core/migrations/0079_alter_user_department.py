# Generated by Django 4.1.5 on 2023-06-04 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0078_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='department', to='core.department'),
        ),
    ]
