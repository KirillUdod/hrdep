from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, FormView
from django.shortcuts import render


from .forms import EmployDocumentForm, DismissDocumentForm
from .models import Staff

# Create your views here.
class IndexView(TemplateView):
    template_name = 'hrdep/index.html'

class EmployDocumentView(FormView):
    template_name = 'hrdep/form.html'
    initial = {'document_type': '0'}
    form_class = EmployDocumentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            doc = form.save()
            doc.document_type = doc.EMPLOYEMENT
            doc.save()
            messages.success(request,
                             "Создан документ %s № %s от %s" %
                             (doc.DOCUMENT_TYPE[doc.EMPLOYEMENT][1], doc, doc.date.strftime('%B %d, %Y')))
            return HttpResponseRedirect(reverse('hrdep:index'))

        return render(request, self.template_name, {'form': form})


class DismissDocumentView(FormView):
    template_name = 'hrdep/form.html'
    form_class = DismissDocumentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            doc = form.save()
            doc.document_type = doc.DISMISSION
            doc.save()
            messages.success(request,
                             "Создан документ %s № %s от %s" %
                             (doc.DOCUMENT_TYPE[doc.DISMISSION][1], doc, doc.date.strftime('%B %d, %Y')))
            return HttpResponseRedirect(reverse('hrdep:index'))

        return render(request, self.template_name, {'form': form})


class ReportView(ListView):
    template_name = 'hrdep/report.html'
    model = Staff

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context['new_staff'] = Staff.objects.all_employed()
        context['dismiss_staff'] = Staff.objects.all_dismissed()
        context['working_staff'] = Staff.objects.all_working()

        return context
