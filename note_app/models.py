from django.db import models
from django.contrib.auth.models import User

# Create your models here.
FILE_TYPE_CHOICES = [
        ('text', 'Text'),
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(null=True)
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    file = models.FileField(upload_to='attachments/', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.owner)




    
    def __str__(self) -> str:
        return self.file_type