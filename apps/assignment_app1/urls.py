from django.conf.urls import url
from . import views

# These are the routes for my apps

urlpatterns = [
    url(r'^$', views.index),
    url(r'new$', views.new),
    url(r'create$', views.create),
    url(r'show/(?P<number>\d+)$', views.show),
    url(r'edit/(?P<number>\d+)$', views.edit),
    url(r'delete/(?P<number>\d+)$', views.destroy)
]


