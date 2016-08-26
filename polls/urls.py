#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<survey_id>\d+)/respond/$',views.respond,name='respond'),
	url(r'^(?P<response_id>\d+)/results/$',views.booya,name='booya'),
)
