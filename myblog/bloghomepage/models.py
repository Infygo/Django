from django.db import models

# Create your models here.

# my base table


class Content(models.Model):
    content = models.CharField(max_length=20)

    def __str__(self):
        return self.content


# child tables

class Cities(models.Model):
    contents = models.ForeignKey(Content, on_delete=models.CASCADE)
    cityname = models.CharField(max_length=20)
    citydescription = models.TextField(max_length=2000)
    cityyear = models.CharField(max_length=4)
    citypics = models.ImageField(upload_to='images/', default='media/images/black.jpg')

    def __str__(self):
        return self.cityname + '\n' + self.citydescription + '\n' + self.cityyear + '\n'


class MoviesSeries(models.Model):
    contents = models.ForeignKey(Content, on_delete=models.CASCADE)
    moviename = models.CharField(max_length=100)
    moviedescription = models.TextField(max_length=2000)
    moviequote = models.CharField(max_length=100)
    moviepic = models.ImageField(upload_to='images/', default='media/images/black.jpg')

    def __str__(self):
        return self.moviename + '\n' + self.moviequote + '\n' + self.moviedescription


class Sports(models.Model):
    contents = models.ForeignKey(Content, on_delete=models.CASCADE)
    player = models.CharField(max_length=50)
    team = models.CharField(max_length=25)
    description = models.TextField(max_length=2000)
    playerpic = models.ImageField(upload_to='images/', default='media/images/black.jpg')

    def __str__(self):
        return self.player + '\n' + self.team + '\n' + self.description


class Thoughts(models.Model):
    contents = models.ForeignKey(Content, on_delete=models.CASCADE)
    thoughts = models.TextField(max_length=10000)
