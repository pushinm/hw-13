# Generated by Django 4.1.5 on 2023-01-17 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0006_teacher_classes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='classes',
        ),
    ]
