from django import forms
from django.utils import timezone

import datetime

from .models import Document, Staff


class DateField(forms.DateField):

    def validate(self, value):
        "Check if value consists only of valid emails."

        # Use the parent's handling of required fields, etc.
        super(DateField, self).validate(value)
        print(value)
        print(timezone.now().date())
        if value > timezone.now().date():
            raise forms.ValidationError('Date is not correct')


class EmployDocumentForm(forms.ModelForm):
    employ_date = DateField(widget=forms.SelectDateWidget,
                            label='Дата приема')
    staff = forms.ModelChoiceField(queryset=Staff.objects.all_new(), label='Сотрудник')

    class Meta:
        model = Document
        fields = ["staff", "employ_date", "number"]


class DismissDocumentForm(forms.ModelForm):
    dismiss_date = DateField(widget=forms.SelectDateWidget, label='Дата увольнения')
    staff = forms.ModelChoiceField(queryset=Staff.objects.all_working(), label='Сотрудник')

    class Meta:
        model = Document

        fields = ["staff", "dismiss_date", "number"]