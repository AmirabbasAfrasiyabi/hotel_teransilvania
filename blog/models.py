from django.db import models

# Create your models here.
class Post(models.Model):
    # image
    title = models.CharField(max_length=100)
    content = models.TextField()
    #tag
    #category
    #author
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True , blank=True )
    updated_date = models.DateTimeField(auto_now=True , blank=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'posts'
        verbose_name_plural = 'posts'


    def __str__(self):
        return "{} - {}".format(self.title , self.id)





