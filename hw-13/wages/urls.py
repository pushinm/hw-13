from django.urls import path
from wages.views import show_teachers_grid, wage_recalculate

app_name = 'wages'

urlpatterns = [
    # общая таблица зарплаты всех учителей
    path('', show_teachers_grid, name='show_teachers_grid'),
    # почему то этот путь не работает, скорее всего из-за того что в views внутри функции show_teachers_grid
    # прописан только 1 случай если нет pk. не учитывается случай когда передается pk. но в шаблоне
    # href="{% url 'wages:show_teachers_grid' teacher_item.pk %}
    path('<int:pk>/', show_teachers_grid, name='show_teachers_grid'),
    # путь для пересчета з.п. учителя
    path('recalculate/<int:pk>/', wage_recalculate, name='wage_recalculate'),
]
