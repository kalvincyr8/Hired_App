from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User

class JobManager(models.Manager):
    def addJob(self, job):
        errors = []
        response = {}
        if len("".join(job[0].split())) < 3:
            errors.append("Please give your Job a name at least 3 characters long.")
        for item in Job.objects.all():
            if "".join(job[0].split()).lower() == "".join(item.title.split()).lower():
            # if "".join(job[0].split()).lower() == "".join(item.info.split()).lower():
                errors.append("Please give your Job a unique name.")
            if "".join(job[0].split()).lower() == "".join(item.info.split()).lower():
                errors.append("Please give a unique Discription")
        if errors:
            response['errors'] = errors
            response['status'] = False
        else:
            response['status']=True
            newJob=Job.objects.create(title=job[0], info=job[1], created_by=User.objects.get(id=job[2]))
            newJob.save()
            newJob.saved_by.add(User.objects.get(id=job[2]))
            response['job']=newJob
        return response
    def deleteJob(self, id):
        errors=[]
        response={}
        job = Job.objects.filter(id=id)
        if job:
            print "****"
            print job[0]
            print "****"
            job[0].delete()
            response['status']=True
        else:
            errors.append("Job wasn't found")
            response['stuats']=False
        return response

    def removeJob(self, id, user_id):
        errors = []
        response = {}
        job = Job.objects.filter(id=id)
        if job:
            job[0].saved_by.remove(User.objects.get(id=user_id))
            response['status']=True
        else:
            errors.append("Job was not found")
            response['status']=False
            response['errors']=errors
        return response

    def add_job(self, id, user_id):
        errors = []
        response = {}
        job = Job.objects.filter(id=id)
        if job:
            print "*****"
            print Job
            print "****"
            job[0].saved_by.add(User.objects.get(id=user_id))
            response['status']=True
        else:
            errors.append("Job was not found")
            response['status']=False
            response['errors']=errors
        return response


class Job(models.Model):
    title = models.CharField(max_length=48)
    info = models.CharField(max_length=240)
    created_by = models.ForeignKey(User, related_name='created_by')
    saved_by = models.ManyToManyField(User, related_name = 'saved_by')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = JobManager()
