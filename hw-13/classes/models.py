from django.db import models

# from teachers.models import Teacher

# Create your models here.


class ClassAbstract(models.Model):
    name = models.CharField(verbose_name='Название предмета', max_length=100)
    
    class Meta:
        abstract = True
        
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
        
    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("classes:class_view", kwargs={"pk": self.pk})

class Class(ClassAbstract):
    name = models.CharField(verbose_name='Название предмета', max_length=100)
    
class ClassWithTeacher(ClassAbstract):
    teacher = models.ManyToManyField(to="teachers.Teacher")
    
    class Meta:
       
        verbose_name = 'Занятие + Учителя'
        verbose_name_plural = 'Занятия + Учителя'
