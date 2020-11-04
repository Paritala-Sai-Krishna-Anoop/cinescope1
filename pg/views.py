from django.shortcuts import render
from.forms import hiringform
from .models import mainman , camera , audio , audioe , videoe
from .filters import audiofilter, videoefilter , jobfilter
def homeview(request):
    return render(request, "index.html")
def courses(request):
    return render(request, "courses.html")
def contact(request):
    return render(request, "contact.html")
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
    return render(request, "home.html")

def moviee(request):
    return render(request, "movieinfo.html")
def costum(request):
    form=hiringform()

    if request.method == 'POST':
        form=hiringform(request.POST)
        if form.is_valid():
            form.save()
    context= {'form':form}
    return render(request,"costum.html", context)
def hired(request):
    form = hiringform()
    objs= mainman.objects.all()
    jobffilter = jobfilter(request.GET, queryset=objs)
    objs = jobffilter.qs

    context = {'form': form,'objs':objs ,'jobffilter':jobffilter}
    return render(request, "want.html",context)


def camee(request):
    obj=camera.objects.all()
    context={'obj':obj}

    return render(request, "camee.html",context)

def audi(request):
    obj = audio.objects.all()
    myFilter = audiofilter(request.GET,queryset=obj)
    obj=myFilter.qs
    context = {'obj': obj , 'myFilter': myFilter}
    return render(request, "audiequip.html",context)

def audioediting(request):
    obj=audioe.objects.all()
    context={'obj':obj}

    return render(request, "audioediting.html",context)


def vide(request):
    obj= videoe.objects.all()
    myveFilter = videoefilter(request.GET, queryset=obj)
    obj = myveFilter.qs
    context = {'obj': obj, 'myveFilter': myveFilter}

    return render(request, "vide.html",context)
