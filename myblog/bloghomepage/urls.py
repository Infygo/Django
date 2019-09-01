
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from bloghomepage import views

app_name = 'bloghomepage'

urlpatterns = [
    path('', views.index, name='index'),   # home page view
    path('<int:content_id>/', views.detail, name='detail'),
    path('<int:content_id>/', views.detail, name='detail_cities'),
    path('<int:content_id>/', views.detail, name='detail_movies'),
    path('<int:content_id>/', views.detail, name='detail_sports'),
    path('<int:content_id>/', views.detail, name='detail_thoughts'),
]
