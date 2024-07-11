from django.contrib import admin
from .models import ToDo, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')
    inlines = [PhotoInline]

admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Photo)
