# Generated by Django 4.0.3 on 2022-05-05 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_alter_dicteduqualifi_edulevelplan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plangraf',
            name='activitykind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activ_kind', to='schedule.dictworkkind', verbose_name='Вид деятельности'),
        ),
        migrations.CreateModel(
            name='EduDirect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Шифр')),
                ('directcode', models.CharField(blank=True, max_length=50, null=True, verbose_name='Код ООП')),
                ('shortname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Краткое название/Префикс')),
                ('fullname', models.CharField(max_length=500, verbose_name='Название')),
                ('durationyear', models.PositiveSmallIntegerField(default=1, verbose_name='СрокЛет')),
                ('durationmonth', models.PositiveSmallIntegerField(default=0, verbose_name='СрокОбученияМесяцев')),
                ('fgosno', models.CharField(blank=True, max_length=50, null=True, verbose_name='НомерДокумента')),
                ('fgosdate', models.DateField(blank=True, null=True, verbose_name='ДатаДокумента')),
                ('attesttype', models.CharField(blank=True, max_length=50, null=True, verbose_name='ТипГОСа')),
                ('programprep', models.PositiveSmallIntegerField(default=0, verbose_name='Программа Подготовки')),
                ('active', models.BooleanField(default=True, verbose_name='Актуальность')),
                ('extid', models.CharField(blank=True, max_length=100, null=True, verbose_name='код Gosinsp')),
                ('parentextid', models.CharField(blank=True, max_length=100, null=True, verbose_name='КодРодительскогоООП Gosinsp')),
                ('edulvl', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='education_lvl', to='schedule.dictedulvl', verbose_name='Уровень образования')),
                ('eduqualifi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='qualification', to='schedule.dicteduqualifi', verbose_name='Квалификация')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule.edudirect', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Направление подготовки',
                'verbose_name_plural': 'Направления подготовки',
            },
        ),
        migrations.AddField(
            model_name='eduprogram',
            name='studydirect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edu_direct', to='schedule.edudirect', verbose_name='Направление/Профиль'),
        ),
    ]
