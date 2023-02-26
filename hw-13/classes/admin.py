from django.contrib import admin
from .models import Class, ClassWithTeacher

# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    # list_display = ('pk', 'name', 'teacher',)
    # list_display_links = ('pk',)
    # search_fields = ('pk', 'name', 'teacher',)
    # list_editable = ('name', 'teacher',)
    pass
    

class ClassWithTeacherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', )
    list_display_links = ('pk',)
    search_fields = ('pk', 'name',)
    list_editable = ('name', )
    pass
    
admin.site.register(Class, ClassAdmin)
admin.site.register(ClassWithTeacher, ClassWithTeacherAdmin)