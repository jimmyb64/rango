from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = self.views * -1
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name
        
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    #last_visit = models.DateTime()
    #first_visit = models.TimeDate()
    
    def __unicode__(self):
        return self.title
        
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)
    def __unicode__(self):
        return self.user.username
        
        