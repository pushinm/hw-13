# Generated by Django 4.1.5 on 2023-01-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0008_teacher_to_class'),
        ('classes', '0002_remove_class_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassWithTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название предмета')),
                ('teacher', models.ManyToManyField(to='teachers.teacher')),
            ],
            options={
                'verbose_name': 'Занятие',
                'verbose_name_plural': 'Занятия',
                'abstract': False,
            },
        ),
    ]
