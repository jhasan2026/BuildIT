from django.contrib import admin
from .models import Project,Payment,Purchase,SalaryPayment,LaborWagePayment,OtherWagePayment,TransportPayment
# Register your models here.


admin.site.register(Project)
admin.site.register(Payment)
admin.site.register(Purchase)
admin.site.register(SalaryPayment)
admin.site.register(LaborWagePayment)
admin.site.register(OtherWagePayment)
admin.site.register(TransportPayment)
