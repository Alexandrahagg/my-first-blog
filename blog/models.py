#importerar modeller för att kunna definera hur ens data ser ut
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User') #this is a link to another model
    title = models.CharField(max_length=200)   #this is how you define text with a limited number of characters
    text = models.TextField() #this is for long text without a limit
    created_date = models.DateTimeField(default=timezone.now) #this is a date and time
    publiched_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title