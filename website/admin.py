from django.contrib import admin
from website.models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('name', 'email', 'subject')
    list_per_page = 50
    ordering = ('-created_date', '-updated_date')

# admin.site.register(Contact)
