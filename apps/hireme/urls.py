from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.index, name="index"),
    url(r'^create', views.create, name='create'),
    url(r'^addJob', views.addJob, name='addJob'),
    # url(r'^removeProduct/(?P<id>\d*)', views.removeProduct, name='removeProduct'),
    # url(r'^wishProduct/(?P<id>\d*)', views.wishProduct, name='wishProduct'),
    url(r'^deleteJob/(?P<id>\d*)', views.deleteJob, name='deleteJob'),
    url(r'^view_user/(?P<user_id>\d*)', views.view_user, name= 'view_user'),
    url(r'^view_job/(?P<id>\d*)', views.view_job, name='view_job'),
    url(r'^add_comment/(?P<job_id>\d*)', views.add_comment, name = 'add_comment'),

    ]
