from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
