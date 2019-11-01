from django.shortcuts import render, get_object_or_404
from .models import Job
# Create your views here.
def nadeem(requrest):
    jobs  = Job.objects
    return render(requrest,'jobs/nadeem.html',{'jobs':jobs})

def detail(requrest,job_id):
    job_detail = get_object_or_404(Job,pk=job_id)
    return render(requrest,'jobs/detail.html',{'job':job_detail})