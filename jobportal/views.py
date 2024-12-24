from django.shortcuts import render, redirect

from .forms import SignUpForm, SignInForm, AddJobForm
from .models import SignUp, SignIn, AddJob

def Sign_up(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'jobportal/sign_up.html', {
            "form": form
        })
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data
            signUp = SignUp.objects.create(
                first_name = date['first_name'],
                last_name = date['last_name'],
                email = date['email'],
                phone_number = date['phone_number'],
                password = date['password'],
            )
            return redirect('sign-in')

    return render(request, 'jobportal/sign_up.html', {
        "form": form
    })

def check(email, password):
    pass

def Sign_in(request):
    if request == 'GET':
        form = SignInForm()
        return render(request, 'jobportal/sign_in.html', {
            "form": form
        })
    else:
        form = SignInForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data
            last_id = SignUp.objects.last()
            if date['password'] == last_id.password and date['email'] == last_id.email:
                signIn = SignIn.objects.create(
                    email = date['email'],
                    password = date['password'],
                )
                return redirect('main-page')
            else:
                return redirect('sign-up')

    return render(request, 'jobportal/sign_in.html', {
        "form": form
    })

def MainPage(request):
    return render(request, 'jobportal/main.html')

def Add_job(request):
    if request.method == "GET":
        form = AddJobForm()
        return render(request, '../templates/jobportal/add_job.html', {
            "form": form
        })
    else:
        form = AddJobForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data
            jobportal = AddJob.objects.create(
                title = date['title'],
                description = date['description'],
                company_name= date['company_name'],
                location = date['location'],
                employment_type= date['employment_type'],
                salary = date['salary'],
                posted_date= date['posted_date'],
            )
            # return redirect('')
    return render(request, '../templates/jobportal/add_job.html', {
        "form": form
    })

def SearchJob(request):
    search =request.GET.get('search')

    if search is None:
        jobs = AddJob.objects.all()

    else:
        jobs = AddJob.objects.filter(title__icontains=search)

    return render(request, '../templates/jobportal/search_job.html', {
        "jobs": jobs, "search": search,
    })


def JobDetails(request, job_id):
    job = AddJob.objects.get(id=job_id)
    return render(request, '../templates/jobportal/job_detail.html', {
        'job': job
    })