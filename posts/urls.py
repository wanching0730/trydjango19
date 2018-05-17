from django.conf.urls import url
from django.contrib import admin

from . import views

# refer to the first come url
urlpatterns = [
    url(r'^$', "posts.views.post_list"),
    url(r'^create/$', "posts.views.post_create"),
    url(r'^detail/$', "posts.views.post_detail"),
    url(r'^update/$', "posts.views.post_update"),
    url(r'^delete/$', "posts.views.post_delete"),

]