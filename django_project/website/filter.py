import django_filters
from job.models import Job
from compete.models import Compete

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job 
        fields = ['title', 'province', 'job_type','industry']
        
class CompeteFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Compete 
        fields = ['title', 'province', 'compete_type','industry']
        
