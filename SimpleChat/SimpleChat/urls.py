"""
Definition of urls for SimpleChat.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from django.urls import path, include 

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    path('', include('app.urls')),

    #url(r'^$', app.views.home, name='home'),
    #url(r'^contact$', app.views.contact, name='contact'),
    #url(r'^about$', app.views.about, name='about'),

    #むりやりエラー消す
    #url(r'^login/$',
    #   app.views.home,
    #    name='login'),
    #url(r'^logout$',
    #    app.views.home,
    #    name='logout'),
    #


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
