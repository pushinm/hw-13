# Generated by Django 4.1.5 on 2023-01-17 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0006_teacher_classes'),
        ('classes', '0002_remove_class_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classes.class', verbose_name='Предмет')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teachers.teacher', verbose_name='Преподаватель')),
            ],
        ),
    ]
