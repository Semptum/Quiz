from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/', views.dashboard, name = "dashboard"),
    url(r'^available/', views.available, name = "available"),
    url(r'^settings/', views.settings, name = "settings"),
    url(r'^login/', views.login, name = "login"),
    url(r'^index/', views.index, name = "index"),
    url(r'^signup/', views.signup, name="signup"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^$', views.index, name = "index"),
]