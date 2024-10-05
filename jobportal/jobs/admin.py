from django.contrib import admin

# Register your models here.
from .models import Company,JobListing,JobApplication

admin.site.register(Company)
admin.site.register(JobListing)
admin.site.register(JobApplication)