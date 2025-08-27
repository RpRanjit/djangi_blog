from django.db import models

# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class EmailTemplate(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject