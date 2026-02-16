from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status', 'published_date', 'created_date', 'updated_date')
    list_filter = ('status', 'published_date', 'created_date', 'updated_date')
    search_fields = ['title', 'content']
    # ordering = ('-created_date', '-updated_date')


# admin.site.register(Post, PostAdmin)
