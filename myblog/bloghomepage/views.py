from django.shortcuts import render
from django.http import HttpResponse , Http404   # for the http request and 404 error
from django.template import loader               # template loader
from .models import Content, Cities, MoviesSeries, Sports, Thoughts
# Create your views here.


# using only templates and render

def index(request):
    all_content = Content.objects.all()
    context = {
        'all_content': all_content
    }

    return render(request, 'bloghomepage/index.html', context)


def detail(request, content_id):
    cont = Content.objects.get(id=content_id)   # filter the content id - to categorize cities, movies, sports
    all_cities = Cities.objects.all()           # retrieve all the cities
    all_movies = MoviesSeries.objects.all()     # retrieve all the movies series
    all_sports = Sports.objects.all()           # retrieve all the sports content
    all_thoughts = Thoughts.objects.all()       # retrieve my posts thoughts

    if content_id == 1:
        context = {
            'cont': cont
        }
        return render(request, 'bloghomepage/detail.html', context)
    elif content_id == 2:
        context = {
            'all_cities': all_cities
        }
        return render(request, 'bloghomepage/detail_cities.html', context)
    elif content_id == 3:
        context = {
            'all_movies': all_movies
        }
        return render(request, 'bloghomepage/detail_movies.html', context)
    elif content_id == 4:
        context = {
            'all_sports': all_sports
        }
        return render(request, 'bloghomepage/detail_sports.html', context)

    elif content_id == 5:
        context = {
            'all_thoughts': all_thoughts
        }
        return render(request, 'bloghomepage/detail_thoughts.html', context)



