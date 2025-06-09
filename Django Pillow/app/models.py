from django.db import models

# Create your models here.
class Blog(models.Model):
    sarlavha = models.CharField(max_length=255)
    xabar = models.TextField()
    rasm = models.ImageField(upload_to="rasmlar/", blank=True)

    def __str__(self):
        return self.sarlavha
    