from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'books'   # for name spacing

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index_books'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='details_books'),
    url(r'books/add/$', views.BooksCreate.as_view(), name='books_add'),  # url for getting into the add book page
]


