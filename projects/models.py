from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    languages = models.CharField(max_length=200, default='')
    image = models.ImageField(default='static/images/default.jpg', upload_to='projects/images/')
    date = models.DateTimeField('date created')
    link = models.URLField(blank=False)
    try_link = models.URLField(blank=True, null=True)

    def languages_as_list(self) -> list[str]:
        return self.languages.replace(' ', '').split(',')

    def __str__(self):
        return self.title
