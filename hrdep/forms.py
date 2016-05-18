from django import forms
from .models import Document


class DocumentEmployForm(forms.ModelForm):
    employ_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Document
        fields = ["staff", "employ_date", "number"]

class DocumentUnemployForm(forms.ModelForm):
    employ_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Document
        fields = ["staff", "employ_date", "number"]