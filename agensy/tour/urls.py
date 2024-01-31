from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('tours/', tours, name='tours'),
    path('info/<slug:slug>', info, name='info'),
    path('contact_form/', contact_form, name='contact_form'),
]