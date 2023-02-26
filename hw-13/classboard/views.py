from django.shortcuts import render, get_object_or_404
from .models import Classboard
from teachers.models import Teacher

# Create your views here.

def classboard_view(request, pk=None) -> render:
    """
    Отображает пару "предмет - учитель" или, при наличии параметрах 
    пути pk, конкретную пару "предмет - учитель"
    """
    
    if not pk:
        template_ = 'classboard_all.html'
        # classboard_all = Classboard.objects.select_related().all().distinct()
        classboard_list = set(Classboard.objects.values_list('class_name', flat=True).distinct())
        
        classboard_all = []

        for list_item in classboard_list:
            classboard_all.append(get_object_or_404(Classboard, pk=list_item))
              
        context = {
            'classboard_all': classboard_all
        }
    else:
        template_ = 'classboard_item.html'
        

        classboard_current = get_object_or_404(Classboard, pk=pk)
        
        teachers = Teacher.objects.select_related().filter(to_class=classboard_current.class_name_id)
        context = {
            'classboard_current': classboard_current,
            'teachers': teachers,
        }
        
    return render(request=request, template_name=template_, context=context)
