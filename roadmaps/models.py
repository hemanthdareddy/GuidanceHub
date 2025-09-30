from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_svg = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Domain(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_svg = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class JobRole(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class RoadmapStep(models.Model):
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    step_number = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_role.name} - Step {self.step_number}: {self.title}"

class Skill(models.Model):
    step = models.ForeignKey(RoadmapStep, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name