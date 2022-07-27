from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post (models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank= True, null = True)
    #content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #separate image form if needed instead of ckeditor
    #image = models.ImageField(null=True, blank= True, upload_to = 'images/') 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



        