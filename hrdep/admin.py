from django.contrib import admin

# Register your models here.
from .models import Document, Post, Staff


class StaffModelAdmin(admin.ModelAdmin):
    readonly_fields = ["employ_date", "dismiss_date"]
    search_fields = ["last_name", "post"]

class DocumentModelAdmin(admin.ModelAdmin):
    readonly_fields = ["date"]

admin.site.register(Staff, StaffModelAdmin)
admin.site.register(Document, DocumentModelAdmin)
admin.site.register(Post)

