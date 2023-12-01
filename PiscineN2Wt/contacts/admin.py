from django.contrib import admin

from .models import Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ('adresse_email','nom', 'message')
    
    
admin.site.register(Contact, PostAdmin)