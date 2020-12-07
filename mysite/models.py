from django.db import models
from phone_field import PhoneField
from ckeditor.fields import RichTextField


# Create your models here.

class Categories(models.Model):
    categories = models.CharField(max_length=100)

    def __str__(self):
        return self.categories


class Tag(models.Model):
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.tags


class Members(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=150)
    description = models.CharField(max_length=250)
    positions = models.CharField(max_length=200, default='member')
    image = models.ImageField(upload_to='members')

    def __str__(self):
        return self.name + " " + self.address


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(Categories)
    tag = models.ManyToManyField(Tag)
    post = RichTextField()
    author = models.ManyToManyField(Members)
    image = models.ImageField(upload_to='post')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()


class Contact(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()
