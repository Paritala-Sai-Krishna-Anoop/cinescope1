from django.shortcuts import render , redirect
from django.template import RequestContext
from.forms import hiringform,joiningform , CreateUserform ,UploadFileForm
from .models import *
from .filters import audiofilter, videoefilter , jobfilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def homeview(request):
    form = joiningform()

    if request.method == 'POST':
        form = joiningform(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "index.html", context)

def courses(request):
    return render(request, "courses.html")
def contact(request):
    return render(request, "login.html")
def vide(request):
    return render(request, "vide.html")
def audioediting(request):
    return render(request, "audioediting.html")
def pricing(request):
    return render(request, "pricing.html")
def trainers(request):
    return render(request, "trainers.html")
def about(request):
    return render(request, "about.html")
def direct(request):
    return render(request, "direction.html")
def home(request):
    form = joiningform()

    if request.method == 'POST':
        form =joiningform(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "home.html",context)

def moviee(request):
    return render(request, "movieinfo.html")
@login_required(login_url='login')
def costum(request):
    form=hiringform()

    if request.method == 'POST':
        form=hiringform(request.POST)
        if form.is_valid():
            form.save()
    context= {'form':form}
    return render(request,"costum.html", context)

@login_required(login_url='login')
def hired(request):
    form = hiringform()
    objs= mainman.objects.all()
    jobffilter = jobfilter(request.GET, queryset=objs)
    objs = jobffilter.qs

    context = {'form': form,'objs': objs, 'jobffilter': jobffilter}
    return render(request, "want.html", context)


def camee(request):
    obj=camera.objects.all()
    context={'obj':obj}

    return render(request, "camee.html",context)

def sws(request):
    obj=sw.objects.all()
    context={'obj':obj}

    return render(request, "sw.html",context)

def audi(request):
    obj = audio.objects.all()
    myFilter = audiofilter(request.GET, queryset=obj)
    obj=myFilter.qs
    context = {'obj': obj, 'myFilter': myFilter}
    return render(request, "audiequip.html", context)

def audioediting(request):
    obj=audioe.objects.all()
    context = {'obj': obj}

    return render(request, "audioediting.html",context)


def vide(request):
    obj= videoe.objects.all()
    myveFilter = videoefilter(request.GET, queryset=obj)
    obj = myveFilter.qs
    context = {'obj': obj, 'myveFilter': myveFilter}

    return render(request, "vide.html",context)


def loginn(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form= CreateUserform()

        context= {'form':form}

        if request.method == 'POST':
            form = CreateUserform(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for  ' +  user)
                return redirect('login')

        return render(request, "signup.html", context)


def loginnn(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.info(request, "username or password is incorrect")
                messages.info(request, 'login failed, please enter correct username and password.')

        return render(request,"login.html")

def LogoutUser(request):
    logout(request)
    return redirect('login')

def  resumeupload(request):
    if request.method=='POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                new_file = UploadFile(file=request.FILES['file'])
                new_file.save()

                return redirect('/')
            else:
                form = UploadFileForm()

            data = {'form': form}
    return render(request,'costum.html', data)