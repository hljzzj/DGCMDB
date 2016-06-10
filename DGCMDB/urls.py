"""DGCMDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
from activator import process
from website.views import index,ApplyCertificate,Login,Adduser,Adddata,Deldata,Update,Getdata


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index,name='index'),
    #('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<page>(\d+))/(?P<id>(\d+))/$', process),
    #('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<id>(\d+))/$', process),
    #('^(?P<app>(\w+))/(?P<function>(\w+))/$', process),
    #('^(?P<app>(\w+))/$', process, {'function': 'index'}),
    #('^$', process, {'function': 'index'}),
    url(r'^AppalyCertificate/$',ApplyCertificate),
    url(r'^login/$',Login),
    url(r'^adduser/$',Adduser),
    url(r'^adddata/(?P<name>\d*)/$',Adddata),
    url(r'^deldata/(?P<id>\d*)/$',Deldata),
    url(r'^update/(?P<id>\d*)/(?P<hostname>\w*)/$',Update),
    url(r'^getdata/(?P<hostname>\w*)/$',Getdata),
)

