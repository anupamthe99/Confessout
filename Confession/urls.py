from django.urls import path
from . import views
from django.contrib import admin
# Django admin customization
admin.site.site_header="Hamro Confession"
admin.site.site_title="Hamro Confession"
admin.site.index_title="Welcome to Hamro Confession Admin Page"
urlpatterns = [
    path('',views.index,name="home"),
    path('confession',views.confession,name="confession"),
    path('colleges',views.colleges,name="colleges"),
    path('contact',views.Contactt,name="contact"),
    path('about',views.about,name="about"),
]