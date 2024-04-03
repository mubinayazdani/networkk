from django.db import models

from django.conf import settings

# Create your models here.

class Post(models.Model):
    
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=2050)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
        
        
    def __str__(self):
        
        return f'{self.title}'
    
    
    
    
class PostFile(models.Model):
    
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    file = models.FileField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        
        verbose_name = 'PostFile'
        verbose_name_plural = 'PostFiles'
        
    
    def __str__(self):
        
        return f'{self.pk}'
    
    
    
class Commet(models.Model):
    
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT, related_name='comments')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # parent = models.ForeignKey(to='self')#not recommended
    comment = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
    def __str__(self):
        
        return f'{self.comment}'
        
        
class Like(models.Model):
    
    post = models.ForeignKey(to=Post, on_delete=models.PROTECT, related_name='likes')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True) #Descriptor
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'