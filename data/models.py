from django.db import models

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    images = models.ImageField(null=True)

    def __str__(self) :
        return self.title