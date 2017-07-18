from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/', views.index, name = "dashboard"),
    url(r'^available/', views.index, name = "available"),
    url(r'^settings', views.index, name = "settings"),
    url(r'^login', views.index, name = "login"),
    url(r'^$', views.index, name = "index"),
]