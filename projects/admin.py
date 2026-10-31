from django.contrib import admin
from .models import Project, Chapter, Task


# Register your models here.
class ChapterInLine(admin.TabularInline):
    model = Chapter
    fk_name = 'project'
    extra = 0
    field = ('title', 'parent', 'status', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'subject', 'deadline', 'date_of_start')
    list_filter = ("project_type",)
    search_fields = ('project',)
    inlines = [ChapterInLine]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'parent', 'status', 'order')
    list_filter = ('status', "project")
    list_editable = ('status', 'order')
    search_fields = ('parent',)
    autocomplete_fields = ("project", 'parent')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'text', 'is_done', 'order')
    list_filter = ('is_done','chapter__project')
    list_editable = ('is_done', )
