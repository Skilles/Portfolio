from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=20)
    image = models.ImageField(upload_to='projects/static/images/', default='projects/static/images/default.jpg')
    date = models.DateTimeField('date created')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
