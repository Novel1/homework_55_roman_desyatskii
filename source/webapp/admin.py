from django.contrib import admin

from webapp.models import ToDo


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'created_at')
    list_filter = ('id', 'title', 'description', 'status', 'created_at')
    search_fields = ('title', 'description', 'status')
    fields = ('title', 'description', 'status', 'created_at')
    readonly_fields = ('id', 'created_at')


admin.site.register(ToDo, ToDoAdmin)
