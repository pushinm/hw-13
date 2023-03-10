# Generated by Django 4.1.5 on 2023-01-24 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0008_teacher_to_class'),
        ('wages', '0011_rename_created_on_wage_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wage',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers_wage', to='teachers.teacher', verbose_name='Преподаватель'),
        ),
    ]
