from django.conf.urls import include, url
from django.contrib import admin

from .views import IndexView, EmployDocumentView, DismissDocumentView, ReportView

urlpatterns = [

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^employ/$', EmployDocumentView.as_view(), name='employ'),
    url(r'^dismiss/$', DismissDocumentView.as_view(), name='dismiss'),
    url(r'^report/$', ReportView.as_view(), name='report'),

]