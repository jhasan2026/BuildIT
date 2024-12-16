from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse

class Jobs(models.Model):  # Inherit from models.Model here
    is_available = models.BooleanField(default=True)
    job_title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=500)
    deal_payment = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    working_day = models.IntegerField(default=0)
    working_hours = models.IntegerField(default=0)
    experience_year = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)

    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)


    def get_absolute_url(self):
        # Return the URL to redirect to after updating the job post.
        return reverse('job-details', kwargs={'pk': self.id})

class Applicant(models.Model):
    full_name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=20,default='')
    address = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    country = models.CharField(max_length=100,default='')
    state = models.CharField(max_length=100,default='')
    zipcode = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg',upload_to='applicant_pic')

    job_id = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    applicant_user = models.ForeignKey(User,on_delete=models.CASCADE)