from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, FormView
from django.shortcuts import render


# Create your views here.
class MainView(TemplateView):
    template_name = "main.html"

class IndexView(TemplateView):
    template_name = "game/index.html"
