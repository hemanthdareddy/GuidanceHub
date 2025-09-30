from django.contrib import admin
from .models import Branch, Domain, JobRole, RoadmapStep, Skill

# Register your models here.
admin.site.register(Branch)
admin.site.register(Domain)
admin.site.register(JobRole)
admin.site.register(RoadmapStep)
admin.site.register(Skill)