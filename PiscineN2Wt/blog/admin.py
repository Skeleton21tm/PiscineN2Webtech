from django.contrib import admin

from .models import MonPost

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'date')
    search_fields = ('title', 'author')
    list_filter = ('author', 'title')
    
admin.site.register(MonPost, PostAdmin)