from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    caption = models.CharField(max_length=500)
    price = models.CharField(max_length=10)
    itemUrl = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title
