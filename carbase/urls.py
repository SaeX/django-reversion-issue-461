# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^make/add/', views.CarMakeCreateView.as_view(), name='carmake_add'),
    url(r'^make/(?P<pk>\d+)/edit/$', views.CarMakeUpdateView.as_view(), name='carmake_edit'),
    url(r'^make/(?P<pk>\d+)/detail/$', views.CarMakeDetailView.as_view(), name='carmake_detail'),
    url(r'^model/add/', views.CarModelCreateView.as_view(), name='carmodel_add'),
    url(r'^model/(?P<pk>\d+)/edit/$', views.CarModelUpdateView.as_view(), name='carmodel_edit'),
    url(r'^model/(?P<pk>\d+)/detail/$', views.CarModelDetailView.as_view(), name='carmodel_detail'),
)