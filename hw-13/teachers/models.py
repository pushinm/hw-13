from django.db import models
from .validators.validators import validate_age
# from classes.models import Class
# from classboard.models import Classboard
# from classboard.models import Classboard
# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    birth_day = models.DateField(verbose_name='Дата рождения', validators=[validate_age])
    email = models.EmailField(verbose_name='e-mail')
    phone = models.CharField(verbose_name='Телефон', max_length=13)
    to_class = models.ManyToManyField(to="classes.Class", through="classboard.Classboard", verbose_name="Предметы", related_name="teachers")
    
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
        
        ordering = ['first_name', 'last_name']
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('teachers:view_teacher', kwargs={'pk' : self.pk})