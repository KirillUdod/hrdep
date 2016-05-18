from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, FormView


from .forms import DocumentEmployForm, DocumentUnmployForm
from .models import Staff

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class DocumentEmployView(FormView):
    template_name = 'form.html'
    #initial = {'document_type': '0'}
    form_class = DocumentEmployForm

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

class DocumentUnemployView(FormView):
    template_name = 'form.html'
    # initial = {'document_type': '1'}
    form_class = DocumentUnmployForm

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

class ReportView(TemplateView):
    template_name = "index.html"
