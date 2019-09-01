from django.shortcuts import render

from django.http import HttpResponse
from .models import Publishers
from django.template import loader
from django.shortcuts import render
from django.http import Http404

# Create your views here.

# Trying to see the data in the index page

# function without templates

# def index_publishers(request):
#     all_publisher = Publishers.objects.all()
#     html_publisher = ''
#
#     for publisher in all_publisher:
#         url = '/publishers/' + str(publisher.id) + '/'
#         html_publisher += '<a href = "' + url + '">' + str(publisher.publisher_name) + '</a><br>'
#
#     return HttpResponse(html_publisher)

# function using templates


def index_publishers(request):
    all_publisher = Publishers.objects.all()

    # template = loader.get_template('publishers/index.html')
    context = {
        'all_publisher': all_publisher
    }

    # return HttpResponse(template.render(context, request))  # using template
    return render(request, 'publishers/index_publishers.html', context)

# another view
# raising a 404 exception


def details_publishers(request, publisher_id):
    try:
        publisher = Publishers.objects.get(id=publisher_id)
    except Publishers.DoesNotExist:
        raise Http404('Publisher doesnt exist')

    # Lets use the template and render this

    template = loader.get_template('publishers/details_publishers.html')
    context = {
        'publisher': publisher
    }
    return HttpResponse(template.render(context, request))

    # return HttpResponse("<h5>Details for the publisher id:" + str(publisher_id) + "</h5>")

