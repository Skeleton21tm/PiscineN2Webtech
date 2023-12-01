from django.db import models

class MonPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(null=False)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=40)
    
    def __str__(self):
        return self.title