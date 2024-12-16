
from django.urls import path, include
from . import views
from .views import JobListView,JobDetailsView, JobCreateView,JobPostUpdateView,MyJobListView,Apply_for_job,ApplicantListView,MyArchiveJobListView


urlpatterns = [
    path('',JobListView.as_view(),name='job-list'),
    path('createdByMe/',MyJobListView.as_view(),name='my-job-list'),
    path('createdByMe/archived/',MyArchiveJobListView.as_view(),name='my-archived-job-list'),
    path('new/',JobCreateView,name='job-create'),
    path('<int:pk>/',JobDetailsView.as_view(),name='job-details'),
    path('<int:pk>/applicant_list/',ApplicantListView.as_view(),name='applicant-list'),
    path('<int:pk>/update/',JobPostUpdateView.as_view(),name='job-update'),
    path('<int:pk>/apply_job/',Apply_for_job,name='apply-job'),
]
