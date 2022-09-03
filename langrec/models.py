from django.db import models


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=25)
    data = models.JSONField(default=dict)
    major = models.BooleanField(default=False)
    url = models.URLField(default="/")

    def __str__(self):
        return self.name

