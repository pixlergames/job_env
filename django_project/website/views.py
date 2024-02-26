from django.shortcuts import render
from job.models import Job,ApplyJob
from .filter import JobFilter
from compete.models import Compete,ApplyCompete
from .filter import CompeteFilter




def home(request):
    filter = JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))
    compete_filter = CompeteFilter(request.GET, queryset=Compete.objects.filter(is_available=True).order_by('-timestamp'))
    context = {'filter': filter, 'compete_filter': compete_filter}
    return render(request, 'website/home.html', context)
# Create your views here.

def job_listing(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs':jobs}
    return render(request, 'website/job_listing.html', context)

def compete_listing(request):
    compete = Compete.objects.filter(is_available=True).order_by('-timestamp')
    context = {'compete':compete}
    return render(request, 'website/compete_listing.html', context)

from django.contrib.auth.decorators import login_required

@login_required
def job_details(request, pk):
    if ApplyJob.objects.filter(user=request.user, job=pk).exists():
        has_applied = True
    else:
        has_applied = False
    job = Job.objects.get(pk=pk)
    context = {'job': job, 'has_applied': has_applied}
    return render(request, 'website/job_details.html', context)

def compete_details(request, pk):
    if ApplyCompete.objects.filter(user=request.user, compete=pk).exists():
        has_applied = True
    else:
        has_applied = False
    compete = Compete.objects.get(pk=pk)
    context = {'compete': compete, 'has_applied': has_applied}
    return render(request, 'website/compete_details.html', context)
