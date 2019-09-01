from django.db import models
from django.core.urlresolvers import reverse

# Create your models here. - represents the backend


class Books(models.Model):

    def get_absolute_url(self):
        return reverse('books:details_books', kwargs={'pk': self.pk})  # return to the details page

    def __str__(self):
        return self.name + '--' + self.author + '--' + self.price + '--' + self.type + '--' + self.book_image

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    book_image = models.CharField(max_length=5000)  # stores the url of the image





