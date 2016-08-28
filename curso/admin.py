#Admin.py da app curso
from django.contrib import admin
from .models import Category, Course


class CoursseAdmin(admin.ModelAdmin):
    list_display = ['name','is_approved']
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_field = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Course,CoursseAdmin)
