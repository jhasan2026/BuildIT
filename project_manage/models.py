from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Project(models.Model):
    project_name = models.CharField(max_length=100,default='')
    project_description = models.CharField(max_length=300,default='')
    client_contact_no = models.CharField(max_length=20,default='')
    project_location = models.CharField(max_length=50,default='')
    project_city = models.CharField(max_length=20,default='')
    project_country = models.CharField(max_length=20,default='')
    project_zip = models.IntegerField(default=0)

    budget = models.IntegerField(default=0)
    deadline = models.DateTimeField(default=timezone.now)
    has_closed = models.BooleanField(default=False)
    has_accepted = models.BooleanField(default=False)
    proposed_date = models.DateTimeField(default=timezone.now)

    client = models.ForeignKey(User,on_delete=models.CASCADE,related_name='project_client')
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='project_owner',default=None,null=True)

class Payment(models.Model):
    purchase_payment = models.IntegerField(default=0)
    labor_wages_payment = models.IntegerField(default=0)
    other_wages_payment = models.IntegerField(default=0)
    salary_payment = models.IntegerField(default=0)
    transport_payment = models.IntegerField(default=0)
    revenue = models.IntegerField(default=0)
    no_of_installment = models.IntegerField(default=1)
    installment_payment = models.IntegerField(default=0)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Purchase(models.Model):
    purchase_title = models.CharField(max_length=50,default='')
    purchase_amount = models.IntegerField(default=0)

    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)

class SalaryPayment(models.Model):
    salary_title = models.CharField(max_length=50,default='')
    salary_amount = models.IntegerField(default=0)

    salary_payment = models.ForeignKey(Payment,on_delete=models.CASCADE)

class LaborWagePayment(models.Model):
    labor_wage_title = models.CharField(max_length=50,default='')
    labor_wage_amount = models.IntegerField(default=0)

    labor_wage_payment = models.ForeignKey(Payment,on_delete=models.CASCADE)

class OtherWagePayment(models.Model):
    other_wage_title = models.CharField(max_length=50,default='')
    other_wage_amount = models.IntegerField(default=0)

    other_wage_payment = models.ForeignKey(Payment,on_delete=models.CASCADE)


class TransportPayment(models.Model):
    transport_title = models.CharField(max_length=50, default='')
    transport_amount = models.IntegerField(default=0)

    transport_payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

