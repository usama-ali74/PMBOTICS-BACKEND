# Generated by Django 4.1.5 on 2023-05-07 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_alter_project_grade_alter_teammember_grade'),
        ('milestone', '0006_milestonemarks_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='milestonefinalmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('marks', models.FloatField(default=50.0)),
                ('milestone', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.milestone')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]