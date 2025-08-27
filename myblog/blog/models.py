from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('News', 'News'),
        ('Sports', 'Sports'),
        ('Politics', 'Politics'),
        ('Technology', 'Technology'),
        ('Lifestyle', 'Lifestyle'),
        ('Business', 'Business'),
        ('Weather', 'Weather')
    ]
    
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=2500, default='default.jpg')
    content = models.TextField()
    description = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='News')  # Changed here
    published_by = models.CharField(max_length=100, default='Editor')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
   posts = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name = 'comments')
   name = models.CharField(max_length=100)
   email = models.EmailField()
   body = models.TextField()
   date = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f'Comment by {self.name} on {self.posts}'
    
