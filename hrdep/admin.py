from django.contrib import admin

# Register your models here.
from .models import Document, Post, Staff


class StaffModelAdmin(admin.ModelAdmin):
    readonly_fields = ["employ_date", "unemploy_date"]
    search_fields = ["last_name", "post"]

admin.site.register(Staff, StaffModelAdmin)
admin.site.register(Document)
admin.site.register(Post)

