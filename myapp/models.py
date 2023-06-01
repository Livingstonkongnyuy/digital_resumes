from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    image = models.ImageField(upload_to = 'media/blog')
    date_created = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Certificate(models.Model):
    titles = models.CharField(max_length=50)
    description = models.TextField()
    date_issued = models.DateField()
    issuer = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to = 'media/certificate')
 
    def __str__(self):
        return self.titles

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificate'

from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    facebook = models.CharField(max_length=2000, null=True, blank=True)
    twitter = models.CharField(max_length=2000, null=True, blank=True)
    linkedin = models.CharField(max_length=2000, null=True, blank=True)
    instagram = models.CharField(max_length=2000, null=True, blank=True)
    image_field = models.ImageField(upload_to='media/personal')
    email = models.EmailField(max_length= 50)
    

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfile'

class Testimonies(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length = 150, null=True, blank=True)
    image = models.ImageField(upload_to = 'media/testimonies')
    content = models.CharField(max_length=275)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonies'
        verbose_name_plural = 'Testimonies'


class Portfolio(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'media/portfolio')
    url = models.CharField(max_length = 200, blank = True)
    date_created = models.DateField(auto_now_add=True)

 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'


# class Talk(models.Model):
    # names = models.CharField(max_length = 200)
    # emails = models.EmailField(max_length = 200)
    # messages = models.TextField()
# 
    # def __str__(self):
        # return self.names
# 
    # class Meta:
        # verbose_name = 'Talk'
        # verbose_name_plural = 'Talk'
# 



class Contact(models.Model):
    location = models.CharField(max_length = 60)
    email = models.EmailField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'


class Services(models.Model):
    title = models.CharField(max_length = 70)
    content = models.TextField()
    image = models.ImageField(upload_to = 'media/services')
    date_created = models.DateField(auto_now_add = True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'