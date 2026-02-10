from django.urls import path
from blog.views import blog_views , blog_single

app_name = 'blog'
urlpatterns = [
    path('' , blog_views , name = 'index'),
    path('single/', blog_single ,name = 'single'),

]
