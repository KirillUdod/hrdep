from datetime import datetime
from django import forms
from django.contrib import admin, messages
from django.core.exceptions import ValidationError

# Register your models here.
from .models import Document, Post, Staff, DoesNotCompute


class StaffModelAdmin(admin.ModelAdmin):
    readonly_fields = ["employ_date", "dismiss_date"]
    search_fields = ["last_name", "post"]
    list_display = ['get_full_name', 'employ_date', 'dismiss_date', 'post']

TEXT_TO_STATUS_INTEGER = {
    u'Прием на работу': 0,
    u'Увольнение': 1,
}


class DocumentCheckedForm(forms.ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        staff = cleaned_data.get('staff')
        employ_date = cleaned_data.get('employ_date')
        dismiss_date = cleaned_data.get('dismiss_date')
        document_type = cleaned_data.get('document_type')
        if document_type == 1 and staff.employ_date is None:
            raise forms.ValidationError(u"%s невозможно уволить. Он не был принят" % staff.get_full_name())
        if employ_date is None and dismiss_date is None:
            raise forms.ValidationError(u"Введите дату приема/увольнения")
        if employ_date is not None and dismiss_date is not None:
            raise forms.ValidationError(u"Не может быть одновременно дата увольнения и приема")
        if document_type == 0 and employ_date is None and dismiss_date is not None:
            raise forms.ValidationError(u"Для документа Приема должна быть дата приема")
        if document_type == 1 and employ_date is not None and dismiss_date is None:
            raise forms.ValidationError(u"Для документа Увольнения должна быть дата увольнения")
        if employ_date is not None:
            if employ_date > datetime.today().date():
                raise forms.ValidationError(u"Дата приема не может быть будущей")
        if dismiss_date is not None:
            if dismiss_date > datetime.today().date():
                raise forms.ValidationError(u"Дата увольнения не может быть будущей")
        return super(DocumentCheckedForm, self).clean()


class DocumentModelAdminForm(DocumentCheckedForm):
    class Meta:
        model = Document
        fields = '__all__'


class DocumentModelAdmin(admin.ModelAdmin):
    form = DocumentModelAdminForm
    search_fields = ['staff__last_name', 'staff__middle_name', 'staff__first_name', "document_type"]
    readonly_fields = ["date"]
    list_display = ['staff', 'document_type', 'date', 'employ_date', 'dismiss_date', 'number']
    list_filter = ['document_type', 'date', 'employ_date', 'dismiss_date']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(DocumentModelAdmin, self).get_search_results(request, queryset, search_term)
        if search_term in TEXT_TO_STATUS_INTEGER:
            queryset |= self.model.objects.filter(document_type=TEXT_TO_STATUS_INTEGER[search_term])
        return queryset, use_distinct

admin.site.register(Staff, StaffModelAdmin)
admin.site.register(Document, DocumentModelAdmin)
admin.site.register(Post)

