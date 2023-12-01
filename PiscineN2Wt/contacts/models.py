from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=90)
    message = models.TextField(null=True)
    adresse_email = models.EmailField(max_length=90)
    def __str__(self):
        return self.nom