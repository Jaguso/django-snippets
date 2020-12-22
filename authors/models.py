from django.db import models


class Authors(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    nationality = models.CharField(max_length=50, default='')

    class Meta: 
        ordering = ['created']