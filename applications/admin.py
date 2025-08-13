from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'applicant', 'applied_at')
    list_filter = ('job', 'applied_at')
    search_fields = ('job__title', 'applicant__username', 'cover_letter')
