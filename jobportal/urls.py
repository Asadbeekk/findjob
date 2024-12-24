from django.urls import path

from .views import Sign_up, Sign_in, MainPage, Add_job, SearchJob, JobDetails
# from . import views

urlpatterns = [
    path('jobportal/signup', Sign_up, name='sign-up'),
    path('jobportal/signin', Sign_in, name='sign-in'),
    path('', MainPage, name='main-page'),
    path('jobportal/addjob', Add_job, name='add-job'),
    path('jobportal/searchjob', SearchJob, name='search-job'),
    path('jobportal/<int:job_id>/', JobDetails, name='job-details'),
]