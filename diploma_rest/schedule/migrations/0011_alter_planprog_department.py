# Generated by Django 4.0.3 on 2022-05-07 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_alter_faculty_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planprog',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plandept', to='schedule.department', verbose_name='Кафедра'),
        ),
    ]