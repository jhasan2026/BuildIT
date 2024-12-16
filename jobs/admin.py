from django.contrib import admin

# Register your models here.

from .models import Jobs,Applicant

admin.site.register(Jobs)
admin.site.register(Applicant)