from django.db import models
from django.urls import reverse

class Book(models.Model):
    title =models.CharField(max_length=200)
    author =models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=5)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book_detail',args=[self.id])

