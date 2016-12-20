from django.conf.urls import url, include
from .views import object_list, object


urlpatterns = [
    url(r'^object/(?P<object_id>[0-9]+)/', object, name='object'),
    url(r'^list/(?P<page_id>[0-9]*)$', object_list, name='object_list'),

]
