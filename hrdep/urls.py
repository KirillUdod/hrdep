from django.conf.urls import include, url
from django.contrib import admin

from .views import IndexView, DocumentEmployView, ReportView

urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^doc/$', DocumentEmployView.as_view(), name='doc'),
    url(r'^report/$', ReportView.as_view(), name='report'),

]