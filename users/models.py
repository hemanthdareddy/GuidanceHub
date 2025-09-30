from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Personal Information
    full_name = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(default='default_pic.jpg', upload_to='profile_pics')
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=50, blank=True)
    
    # Academic Details
    college = models.CharField(max_length=100, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)
    academic_status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'