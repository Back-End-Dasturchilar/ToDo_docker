from django.contrib import admin

from todo.models import Todo


# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed')
    list_display_links = ('id', 'title', 'is_completed')
    search_fields = ('title',)


admin.site.register(Todo, TodoAdmin)
