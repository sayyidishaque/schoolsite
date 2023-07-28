from django.contrib import auth, messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import safe

from .models import Registration, Department, Courses
from .forms import RegistrationForm
from django.contrib.auth.models import User


# virtualenv school
# username and password in ishaque both are same
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'user logged in')
            return redirect('/')
        else:
            messages.info(request, 'Invalid username/password')
            return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')


def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Registration Successful')
            return redirect('school:registration')
        else:
            messages.info(request, 'Registration Faild')
    return render(request, 'registration.html', {'form': form})


def load_course(request):
    department_id = request.GET.get('department_id')
    course = Courses.objects.filter(department_id=department_id)
    return render(request, 'dropdown_option.html', {'course': course})
    # return JsonResponse(list(course.values('id', 'name')), safe=False)
