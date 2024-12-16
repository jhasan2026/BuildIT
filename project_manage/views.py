from django.shortcuts import render,redirect
from datetime import datetime
from .models import Project,Payment,Purchase,SalaryPayment,LaborWagePayment,OtherWagePayment,TransportPayment
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

@login_required
def DashboardView(request):
    return render(request,template_name='project_manage/dashboard.html')

@login_required
def AddProject(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_description = request.POST.get('project_description')
        client_contact_no = request.POST.get('client_contact_no')
        project_location = request.POST.get('project_location')
        project_city = request.POST.get('project_city')
        project_country = request.POST.get('project_country')
        project_zip = int(request.POST.get('project_zip'))


        deadline_str = request.POST.get('deadline')

        deadline = ''

        if deadline_str:
            try:
                deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()  # Use .date() to get a date object
            except ValueError:
                # Handle invalid date format
                deadline = None


        project = Project.objects.create(
            project_name=project_name,
            project_description=project_description,
            client_contact_no=client_contact_no,
            project_location=project_location,
            project_city=project_city,
            project_country=project_country,
            project_zip=project_zip,
            deadline=deadline,
            client=request.user,
        )
        if project is not None:
            return redirect('posts-home')
        else:
            messages.error(request, 'Something went wrong for The Post')
    return render(request,template_name='project_manage/add_project.html')


class ProjectProposedListView(LoginRequiredMixin,ListView):
    model = Project
    template_name = 'project_manage/proposed_projects.html'
    context_object_name = 'projects'
    ordering = ['-proposed_date']
    paginate_by = 5

    def get_queryset(self):
        return Project.objects.filter(has_accepted=False).order_by('-proposed_date')

class OurProjectListView(LoginRequiredMixin,ListView):
    model = Project
    template_name = 'project_manage/proposed_projects.html'
    context_object_name = 'projects'
    ordering = ['-proposed_date']
    paginate_by = 5

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user).order_by('-proposed_date')


class ProjectProposedDetailView(LoginRequiredMixin,DetailView):
    model = Project
    template_name = 'project_manage/project_deatils.html'
    context_object_name = 'project'


def AcceptProjectView(request, project_id):
    # For now, let's assume the budget is passed with the request (e.g., via a form or POST method).

    if request.method == "POST":
        budget = int(request.POST.get('budget'))
        purchase_payment = int(request.POST.get('purchase_payment'))
        labor_wages_payment = int(request.POST.get('labor_wages_payment'))
        other_wages_payment = int(request.POST.get('other_wages_payment'))
        salary_payment = int(request.POST.get('salary_payment'))
        transport_payment = int(request.POST.get('transport_payment'))
        no_of_installment = int(request.POST.get('no_of_installment'))
        # Using get_object_or_404 to handle the case when the project does not exist
        project_find = get_object_or_404(Project, id=project_id)

        # Update project attributes
        project_find.owner = request.user
        project_find.budget = budget
        project_find.has_accepted = True
        project_find.save()

        payment = Payment.objects.create(
            purchase_payment=purchase_payment,
            labor_wages_payment=labor_wages_payment,
            other_wages_payment=other_wages_payment,
            salary_payment=salary_payment,
            transport_payment=transport_payment,
            no_of_installment=no_of_installment,
            project=project_find,
        )
        if payment is not None and project_find is not None:
            return redirect('proposed-projects')
        else:
            messages.error(request, 'Something went wrong for The Post')
    return render(request, 'project_manage/accept_proposal.html', {'error': 'Invalid budget'})


class AccountList(LoginRequiredMixin,ListView):
    model = Payment
    template_name = 'project_manage/accounts.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_queryset(self):
        return Payment.objects.filter(project__owner=self.request.user)


class PaymentsDetailsView(LoginRequiredMixin, TemplateView):
    template_name = 'project_manage/payment_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get('project_id')

        # Filter Purchase objects
        context['purchases'] = Purchase.objects.filter(
            payment__project__owner=self.request.user,
            payment__project_id=project_id
        )

        # Filter SalaryPayment objects
        context['salaries'] = SalaryPayment.objects.filter(
            salary_payment__project__owner=self.request.user,
            salary_payment__project_id=project_id
        )

        # Filter SalaryPayment objects
        context['laborWages'] = LaborWagePayment.objects.filter(
            labor_wage_payment__project__owner=self.request.user,
            labor_wage_payment__project_id=project_id
        )

        # Filter SalaryPayment objects
        context['otherWagePayments'] = OtherWagePayment.objects.filter(
            other_wage_payment__project__owner=self.request.user,
            other_wage_payment__project_id=project_id
        )
        # Filter SalaryPayment objects
        context['transportPayments'] = TransportPayment.objects.filter(
            transport_payment__project__owner=self.request.user,
            transport_payment__project_id=project_id
        )

        return context


@login_required
def add_purchase(request,project_id):
    payment = get_object_or_404(Payment,project_id=project_id)
    if request.method == 'POST':
        purchase_title = request.POST.get('purchase_title')
        purchase_amount = int(request.POST.get('purchase_amount'))

        Purchase.objects.create(
            purchase_title=purchase_title,
            purchase_amount=purchase_amount,
            payment=payment
        )

        # Redirect or render success page after saving the purchase
        return redirect('accounts')  # Replace with the desired URL name or path

        # Render a form template if the request method is GET
    return render(request, 'project_manage/payment_details.html', {'project_id': project_id})

@login_required
def add_salary(request,project_id):
    salary_payment = get_object_or_404(Payment,project_id=project_id)
    if request.method == 'POST':
        salary_title = request.POST.get('salary_title')
        salary_amount = int(request.POST.get('salary_amount'))

        SalaryPayment.objects.create(
            salary_title=salary_title,
            salary_amount=salary_amount,
            salary_payment=salary_payment
        )

        # Redirect or render success page after saving the purchase
        return redirect('accounts')  # Replace with the desired URL name or path

        # Render a form template if the request method is GET
    return render(request, 'project_manage/payment_details.html', {'project_id': project_id})


@login_required
def add_labor_wage(request,project_id):
    labor_wage_payment = get_object_or_404(Payment,project_id=project_id)
    if request.method == 'POST':
        labor_wage_title = request.POST.get('labor_wage_title')
        labor_wage_amount = int(request.POST.get('labor_wage_amount'))

        LaborWagePayment.objects.create(
            labor_wage_title=labor_wage_title,
            labor_wage_amount=labor_wage_amount,
            labor_wage_payment=labor_wage_payment
        )

        # Redirect or render success page after saving the purchase
        return redirect('accounts')  # Replace with the desired URL name or path

        # Render a form template if the request method is GET
    return render(request, 'project_manage/payment_details.html', {'project_id': project_id})


@login_required
def add_other_labor_wage(request,project_id):
    other_wage_payment = get_object_or_404(Payment,project_id=project_id)
    if request.method == 'POST':
        other_wage_title = request.POST.get('other_wage_title')
        other_wage_amount = int(request.POST.get('other_wage_amount'))

        OtherWagePayment.objects.create(
            other_wage_title=other_wage_title,
            other_wage_amount=other_wage_amount,
            other_wage_payment=other_wage_payment
        )

        # Redirect or render success page after saving the purchase
        return redirect('accounts')  # Replace with the desired URL name or path

        # Render a form template if the request method is GET
    return render(request, 'project_manage/payment_details.html', {'project_id': project_id})

@login_required
def add_transport_payment(request,project_id):
    transport_payment = get_object_or_404(Payment,project_id=project_id)
    if request.method == 'POST':
        transport_title = request.POST.get('transport_title')
        transport_amount = int(request.POST.get('transport_amount'))

        TransportPayment.objects.create(
            transport_title=transport_title,
            transport_amount=transport_amount,
            transport_payment=transport_payment
        )

        # Redirect or render success page after saving the purchase
        return redirect('accounts')  # Replace with the desired URL name or path

        # Render a form template if the request method is GET
    return render(request, 'project_manage/payment_details.html', {'project_id': project_id})
