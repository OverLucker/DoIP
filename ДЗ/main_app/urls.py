"""ДЗ URL Configuration"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.events_page, name='eventsMainPage'),
    #url(r'^$', views.events_page, name='eventsMainPage'),
    url(r'^page=(?P<page_id>[0-9]+)$', views.events_page_part, name='eventsPage'),
    url(r'^id=(?P<id>[0-9]+)$', views.event_page, name='event'),
] 
