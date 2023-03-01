from django.db import models

# Create your models here.
class NewsItem(models.Model):
    source = models.CharField(max_length=100)
    link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link[0:50]
    