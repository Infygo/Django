from django.db import models

# Create your models here.


class Publishers(models.Model):

    def __str__(self):
        return self.publisher_name + '--' + self.publisher_location

    publisher_name = models.CharField(max_length=100)
    publisher_location = models.CharField(max_length=5)


