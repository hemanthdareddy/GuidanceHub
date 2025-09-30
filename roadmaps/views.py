# roadmaps/views.py

from django.shortcuts import render
from .models import Branch, Domain, JobRole, RoadmapStep

def branch_list_view(request):
    # 1. Get all branch objects from the database
    branches = Branch.objects.all()
    
    # 2. Create a context dictionary to pass the data to the template
    context = {
        'branch_list': branches
    }
    
    # 3. Render the template with the data and return it
    return render(request, 'roadmaps/branch_list.html', context)
def domain_list_view(request, branch_id):
    # 1. Get the specific branch the user clicked on
    branch = Branch.objects.get(id=branch_id)
    
    # 2. Get all domains that belong to that branch
    domains = Domain.objects.filter(branch=branch)
    
    # 3. Pass the branch and its domains to the template
    context = {
        'branch': branch,
        'domain_list': domains
    }
    
    return render(request, 'roadmaps/domain_list.html', context)
def job_role_list_view(request, domain_id):
    domain = Domain.objects.get(id=domain_id)
    job_roles = JobRole.objects.filter(domain=domain)
    context = {
        'domain': domain,
        'job_role_list': job_roles
    }
    return render(request, 'roadmaps/job_role_list.html', context)
def roadmap_detail_view(request, job_role_id):
    job_role = JobRole.objects.get(id=job_role_id)
    # Get all steps for this job role, ordered by step number
    roadmap_steps = RoadmapStep.objects.filter(job_role=job_role).order_by('step_number')
    
    context = {
        'job_role': job_role,
        'roadmap_steps': roadmap_steps,
    }
    return render(request, 'roadmaps/roadmap_detail.html', context)