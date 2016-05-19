from django.contrib import admin

# Register your models here.
from .models import Document, Post, Staff


class StaffModelAdmin(admin.ModelAdmin):
    readonly_fields = ["employ_date", "dismiss_date"]
    search_fields = ["last_name", "post"]


TEXT_TO_STATUS_INTEGER = {
    u'Прием на работу': 0,
    u'Увольнение': 1,
}


class DocumentModelAdmin(admin.ModelAdmin):
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

