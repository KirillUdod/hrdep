from django import forms
from django.utils import timezone

from datetime import datetime

from .models import Document, Staff


class DateField(forms.DateField):

    def validate(self, value):
        super(DateField, self).validate(value)
        if value > timezone.now().date():
            raise forms.ValidationError('Date is not correct')


class EmployDocumentForm(forms.ModelForm):
    employ_date = DateField(widget=forms.SelectDateWidget,
                            label='Дата приема',
                            initial=datetime.today().date())
    staff = forms.ModelChoiceField(queryset=Staff.objects.all_new(), label='Сотрудник')

    class Meta:
        model = Document
        fields = ["staff", "employ_date", "number"]


class DismissDocumentForm(forms.ModelForm):
    dismiss_date = DateField(widget=forms.SelectDateWidget,
                             label='Дата увольнения',
                             initial=datetime.today().date())
    staff = forms.ModelChoiceField(queryset=Staff.objects.all_working(), label='Сотрудник')

    class Meta:
        model = Document

        fields = ["staff", "dismiss_date", "number"]