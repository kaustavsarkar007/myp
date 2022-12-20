from django.db import models
from django.utils.timezone import now
from tinymce.models import HTMLField

# Create your models here.
class FootPost(models.Model):
    slug = models.CharField(max_length=50)
    sno = models.AutoField(primary_key=True)
    title = models.TextField(max_length=120)
    author = models.CharField(max_length=50)
    content = HTMLField()
    timestamp = models.DateTimeField(blank=True)
    
    def __str__(self) -> str:
        return self.title + "by" + self.author