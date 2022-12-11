from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Apply
from .forms import AddJobForm, ApplyForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def job_details(request, job_id):
    job_det = Job.objects.get(pk=job_id)
    return render(request, 'jobs/job_details.html', {'job_det': job_det})


@login_required
@staff_member_required
def add_job(request):
    if request.method == "POST":
        form = AddJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            return redirect('job_dashboard')
    else:
        form = AddJobForm()
    return render(request, 'jobs/add_job.html', {'form': form})


@login_required
def apply_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == "POST":
        form = ApplyForm(request.POST)
        if form.is_valid():
            applied = form.save(commit=False)
            applied.job = job
            applied.created_by = request.user
            applied.save()
            return redirect('job_dashboard')
    else:
        form = ApplyForm()
    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})


@login_required
@staff_member_required
def recieved_apps(request):
    return render(request, 'jobs/recieved_apps.html')


@login_required
def applied_jobs(request):
    return render(request, 'jobs/applied_jobs.html')


@login_required
def view_applied_job(request, job_id):
    job = get_object_or_404(Apply, pk=job_id, created_by=request.user)
    return render(request, 'jobs/view_applied_job.html', {'job': job})
