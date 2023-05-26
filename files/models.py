from django.db import models

class Files(models.Model):
    title = models.CharField(max_length=255, default='no title')
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.title

class Editor(models.Model):
    source = models.TextField()
    result = models.TextField()
    empty_views=models.CharField(max_length=255)
    command = models.CharField(max_length=255)

    def __str__(self):
        return self.command