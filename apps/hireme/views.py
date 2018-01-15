from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job
from ..login_reg.models import User


def index(request):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.ERROR, "Please login.")
        return redirect('/')
    context = {
    'my_jobList': Job.objects.filter(created_by=User.objects.get(id=request.session['user_id'])),
    'jobList':Job.objects.exclude(created_by=User.objects.get(id=request.session['user_id']))
    }
    return render(request, "hireme/index.html", context)


def create(request):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.ERROR, "Please login.")
        return redirect('/index')

    return render(request, "hireme/create.html")


def addJob(request):
    if not request.method == 'POST':
        messages.add_message(request, messages.ERROR, "Please submit the form.")
        return redirect('/index')
    newJob = Job.objects.addJob([request.POST['jobTitle'], request.POST['jobInfo'], request.session['user_id']])
    if not newJob['status']:
        for error in newJob['errors']:
            messages.add_message(request, messages.ERROR, error)
    else:
        messages.add_message(request, messages.SUCCESS, "Your Job has been added.")

    return redirect('/index')

def deleteJob(request, id):
    if not request.method == 'POST':
        messages.add_message(request, messages.ERROR, "Please submit the form.")
        return redirect('/index')
    result = Job.objects.deleteJob(id)
    if not result['status']:
        for error in result['errors']:
            messages.add_message(request, messages.ERROR, error)
    else:
        messages.add_message(request, messages.SUCCESS, "Your job has been deleted.")
    return redirect('/index')

def view_user(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    # comments = Comment.objects.filter(user__id = user_id)
    context = {
        'my_jobList': Job.objects.filter(created_by=User.objects.get(id=request.session['user_id'])),
    }
    return render(request, 'hireme/view_user.html', context)



def view_job(request, id):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.ERROR, "Please login.")
        return redirect('/')
    # comments = Comment.objects.filter(job__id = job_id).order_by("-created_at")

    context = {
    'job':Job.objects.filter(id=id),
    'jobList':Job.objects.exclude(created_by=User.objects.get(id=request.session['user_id']))

    }
    return render(request, 'hireme/view_job.html', context)


def add_comment(request, job_id):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == 'POST':
        user_id = request.session['user_id']
        B1 = Comment.objects.add_comment(job_id, user_id, request.POST)
        for errors in B1[1]:
            messages.add_message(request, messages.INFO ,error)
        return redirect('/view_job')
