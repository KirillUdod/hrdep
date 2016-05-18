from django import forms
from .models import Document, Staff
from django.db.models import Q


class EmployDocumentForm(forms.ModelForm):
    employ_date = forms.DateField(widget=forms.SelectDateWidget)
    staff = forms. ModelChoiceField(queryset=Staff.objects.all_new())
    class Meta:
        model = Document
        fields = ["staff", "employ_date", "number"]

class DismissDocumentForm(forms.ModelForm):
    dismiss_date = forms.DateField(widget=forms.SelectDateWidget)
    staff = forms. ModelChoiceField(queryset=Staff.objects.all_working())
    class Meta:
        model = Document

        fields = ["staff", "dismiss_date", "number"]