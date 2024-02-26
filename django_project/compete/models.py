from django.db import models
from users.models import User
from company.models import Company
from resume.models import Resume

class Province(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Industry(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Compete(models.Model):
    compete_type_choices = (
        ('Coding/Programming','Coding/Programming'),
        ('Innovation/Startup','Innovation/Startup'),
        ('Design/UX','Design/UX')
        
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length= 100)
    salary = models.PositiveIntegerField(default =35000 )
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    is_available = models.BooleanField(default=True) # if compete is available or not
    timestamp = models.DateTimeField(auto_now_add=True)
    industry = models.ForeignKey(Industry, on_delete = models.DO_NOTHING, null = True, blank = True)
    province = models.ForeignKey(Province, on_delete= models.DO_NOTHING, null = True, blank= True)
    compete_type = models.CharField(max_length=20, choices = compete_type_choices, null = True, blank = True)
    
    def __str__(self):
        return self.title
# Create your models here.

class ApplyCompete(models.Model):
    status_choices = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    compete = models.ForeignKey(Compete, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices = status_choices)
    
