
from django.urls import path, include
from .views import DashboardView,AddProject,ProjectProposedListView,ProjectProposedDetailView,OurProjectListView,AcceptProjectView,AccountList,PaymentsDetailsView,add_purchase,add_salary,add_labor_wage,add_other_labor_wage,add_transport_payment

urlpatterns = [
    path('',DashboardView,name='project-dashboard'),
    path('new/',AddProject,name='add-project'),
    path('proposed_list/',ProjectProposedListView.as_view(),name='proposed-projects'),
    path('our_projects/',OurProjectListView.as_view(),name='our-projects'),
    path('<int:pk>/',ProjectProposedDetailView.as_view(),name='project-details'),
    path('<int:project_id>/accept/', AcceptProjectView, name='proposal-accept'),
    path('accounts/', AccountList.as_view(), name='accounts'),
    path('accounts/<int:project_id>/', PaymentsDetailsView.as_view(), name='accounts-details'),
    path('accounts/<int:project_id>/add_purchase/', add_purchase, name='add-purchase'),
    path('accounts/<int:project_id>/add_salary/',add_salary , name='add_salary'),
    path('accounts/<int:project_id>/add_labor_wage/',add_labor_wage , name='add_labor_wage'),
    path('accounts/<int:project_id>/add_other_labor_wage/',add_other_labor_wage , name='add_other_labor_wage'),
    path('accounts/<int:project_id>/add_transport_payment/',add_transport_payment , name='add_transport_payment'),

]