from django.shortcuts import render
from .models import Job

def dashboard(request):
    jobs = Job.objects.filter(applicant=request.user)

    context = {
        'jobs': jobs
    }

    return render(request, 'dashboard/dashboard.html', context)