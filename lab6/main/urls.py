from django.conf.urls import url, include
from .views import ObjectListView, ObjectView


urlpatterns = [
    url(
        r'^object/(?P<object_id>[0-9]+)/',
        ObjectView.as_view(),
        name='object'
    ),

    url(
        r'^list/(?P<page_id>[0-9]*)$',
        ObjectListView.as_view(),
        name='object_list'
    ),

]
