
from django.urls import path
from django.contrib import admin
from rango import views
from django.conf.urls import url
from django.conf.urls import include

app_name = 'rango'

urlpatterns = [

    url(r'^$',views.index,name='index'),
    path('about/', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category,name='show_category'),
]
