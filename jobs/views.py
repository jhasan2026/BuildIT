from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,UpdateView
from django.contrib import messages
# Create your views here.
from .models import Jobs,Applicant
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required

class JobListView(LoginRequiredMixin,ListView):
    model = Jobs
    template_name = 'jobs/job_dashboard.html'
    context_object_name = 'jobs'
    ordering = ['date_posted']
    paginate_by = 5

    login_url = '/login/'

    def get_queryset(self):
        return Jobs.objects.filter(is_available= True).exclude(posted_by=self.request.user).order_by('-date_posted')

class ApplicantListView(LoginRequiredMixin,ListView):
    model = Applicant
    template_name = 'jobs/applicant_list.html'
    context_object_name = 'applicants'

    def get_queryset(self):
        curr_job_id = self.kwargs.get('pk')
        curr_job = get_object_or_404(Jobs,id=curr_job_id)
        return Applicant.objects.filter(job_id=curr_job)



class MyJobListView(LoginRequiredMixin,ListView):
    model = Jobs
    template_name = 'jobs/my_job_dashboard.html'
    context_object_name = 'jobs'
    ordering = ['date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user,is_available=True).order_by('-date_posted')

class MyArchiveJobListView(LoginRequiredMixin,ListView):
    model = Jobs
    template_name = 'jobs/my_job_dashboard_archived.html'
    context_object_name = 'jobs'
    ordering = ['date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user,is_available=False).order_by('-date_posted')




class JobDetailsView(LoginRequiredMixin,DetailView):
    model = Jobs
    template_name = 'jobs/job_details.html'
    context_object_name = 'job'

@login_required
def JobCreateView(request):
    if request.method == "POST":
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        location = request.POST.get('location')
        deal_payment = int(request.POST.get('deal_payment'))
        working_day = int(request.POST.get('working_day'))
        working_hours = int(request.POST.get('working_hours'))
        experience_year = int(request.POST.get('experience_year'))
        is_available = bool(request.POST.get('is_available'))

        job_post = Jobs.objects.create(
            job_title=job_title,
            job_description=job_description,
            location=location,
            deal_payment=deal_payment,
            working_day=working_day,
            working_hours=working_hours,
            is_available=is_available,
            experience_year=experience_year,
            posted_by=request.user,

        )
        if job_post is not None:
            return redirect('job-list')
        else:
            messages.error(request, 'Something went wrong for The Post')
    return render(request, 'jobs/create_job.html')




class JobPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Jobs
    fields = ['job_title', 'job_description', 'location', 'working_day', 'is_available', 'experience_year']
    template_name = 'jobs/job_update.html'

    def form_valid(self, form):
        form.instance.posted_by = self.request.user  # Make sure the author field is set to the logged-in user
        return super().form_valid(form)

    def test_func(self):
        # Check if the current user is the author of the job post (or has permission to edit)
        job_post = self.get_object()  # Get the current job post
        return job_post.posted_by == self.request.user  # Compare the author field with the logged-in user


@login_required
def Apply_for_job(request,pk):
    job = get_object_or_404(Jobs, pk=pk)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zipcode = int(request.POST.get('zipcode'))
        experience = int(request.POST.get('experience'))
        image = request.FILES.get('image')

        job_apply = Applicant.objects.create(
            full_name=full_name,
            email=email,
            address=address,
            city=city,
            phone=phone,
            country=country,
            state=state,
            zipcode=zipcode,
            experience=experience,
            job_id= job,
            applicant_user=request.user,
            image=image,
        )
        if job_apply is not None:
            return redirect('job-list')
        else:
            messages.error(request, 'Something went wrong for The Post')
    return render(request,'jobs/apply_job.html',{'job':job})




