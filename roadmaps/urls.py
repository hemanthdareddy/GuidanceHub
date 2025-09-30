# roadmaps/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.branch_list_view, name='branch-list'),
    path('branch/<int:branch_id>/', views.domain_list_view, name='domain-list'),
    path('domain/<int:domain_id>/', views.job_role_list_view, name='job-role-list'),
    path('job-role/<int:job_role_id>/', views.roadmap_detail_view, name='roadmap-detail'),
]