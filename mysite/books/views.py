from django.shortcuts import render

# Create your views here. - represents the front end

from django.http import HttpResponse
from .models import Books
from django.template import loader
from django.shortcuts import render
from django.http import Http404


# html function - without the templates

# def index_books(request):
#     all_books = Books.objects.all()
#     html_books = ''
#     for book in all_books:
#         url = '/books/' + str(book.id) + '/'
#         html_books += '<a href="' + url + '">' + str(book.name) + '</a><br>'  #referencing the url to the name of book
#     return HttpResponse(html_books)

# html function - using templates

# def index_books(request):
#     all_books = Books.objects.all()
#     # template = loader.get_template('books/index.html')  # reach the index.html first - no need if using render
#     context = {
#         'all_books': all_books                          # have the data in the context
#     }

    # render the template and context in the response - without render

    # return HttpResponse(template.render(context, request))

    # return render(request, 'books/index_books.html', context)  # using render

# creating another view
# raising an 404 exception


# def details_books(request, book_id):
#     try:
#         book = Books.objects.get(id=book_id)
#     except Books.DoesNotExist:
#         raise Http404('This book doesn\'t exist')
#     template = loader.get_template('books/details_books.html')
#     context = {
#         'book': book
#     }

    # return HttpResponse("<h2>Details for the Book Id:" + str(book_id) + "</h2>")

    # return render(request, '/books/details.html', {'book': book})  # only render
    # return HttpResponse(template.render(context, request))  # using template


# ---------------------------------------------------------------------------------------

# implementing Generic views

from django.views import generic  # generic module
from .models import Books
from django.views.generic.edit import CreateView  # for the create view


class IndexView(generic.ListView):  # for the index html
    template_name = 'books/index_books.html'  # location of the html file

    def get_queryset(self):
        return Books.objects.all()


class BooksCreate(CreateView):
    model = Books
    fields = ['name', 'author', 'price', 'type', 'book_image']


class DetailsView(generic.DetailView):
    model = Books
    template_name = 'books/details_books.html'







