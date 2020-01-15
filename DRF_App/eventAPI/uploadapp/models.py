from django.db import models

class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name
