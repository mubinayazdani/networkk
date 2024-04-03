from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 

# Create your models here.

class Country(models.Model):
    
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        db_table = 'countries'


class Profile(models.Model):
    
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(blank=True, null=True, unique=True)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, upload_to='profile_avatars/')
    
    
    
class Device(models.Model):
    
    WEB = 1
    IOS = 2
    ANDROID = 3
    PC = 4
    
    DEVICE_TYPE_CHOCES = (
        
        (WEB,'web'),
        (IOS,'ios'),
        (ANDROID,'android'),
        (PC, 'pc')
    )
    
    
    
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='deevices',on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device UUID',null=True )
    last_login = models.DateTimeField('last login date',null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOCES,default=ANDROID)
    device_os = models.CharField( max_length=50,blank=True )
    device_model = models.CharField( max_length=50,blank=True)
    app_version = models.CharField( max_length=50,blank=True)
    
    
    
    class Meta:
        
        db_table = 'user_devices'
        verbose_name = 'device'
        verbose_name_plural = 'devices'