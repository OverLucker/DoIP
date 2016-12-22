# Local urls

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register', RegistrationView.as_view(), name='register'),
    url(r'^auth', AuthorizationView.as_view(), name='auth'),
    url(r'^$', index, name='index'),
]
