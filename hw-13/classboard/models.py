from django.db import models

from teachers.models import Teacher
from classes.models import Class

# Create your models here.

class Classboard(models.Model):
    teacher = models.ForeignKey(verbose_name="Преподаватель", to=Teacher, on_delete=models.DO_NOTHING)
    class_name = models.ForeignKey(verbose_name="Предмет", to=Class, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Классная доска'
        verbose_name = 'Расписание'
        
        ordering = ['class_name', 'teacher']
        
    def __str__(self) -> str: 
        return f'{self.class_name} - {self.teacher}'