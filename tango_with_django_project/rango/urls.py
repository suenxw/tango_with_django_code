
from django.urls import path
from django.contrib import admin
from rango import views
from django.conf.urls import url
from django.conf.urls import include

app_name = 'rango'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    url(r'^add_category/$',views.add_category,name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),

]
