from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns("",
    url(r'^cat/([-\w]+)/$', views.single_category, name="single_category"),
    url(r'^$', views.home, name="home"),





    )
