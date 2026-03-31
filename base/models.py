from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    content=models.TextField(max_length=400)
    number=models.CharField(max_length=13)


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField()
    live_link = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title
