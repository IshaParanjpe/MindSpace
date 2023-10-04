from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import RecForms, BlogForms
from .models import Blog, Journaling, Profile, Rec, Therapy
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    # try:
    #     data = Specialskills.objects.all()
    #     context = {"special":data}
    # except Exception as e:
    #     context = {"special": "Not found"}
    return render(request,'index.html')

def support(request):
    return render(request,'support.html')

def meditation(request):
    return render(request,'meditation.html')

def journaling(request):
    if request.method == 'POST':
        proj = Journaling()
        proj.date = request.POST['date']
        proj.day = request.POST['day']
        proj.text = request.POST['text']
        proj.save()
    return render(request,'journaling.html')

def timetable(request):
    return render(request,'timetable.html')

def therapy(request):
     try:
        data = Therapy.objects.all()
        context = {"the":data}
     except Exception as e:
        context = {"the":"Data not found"}
     return render(request,'therapy.html',context)

def contact(request):
    return render(request,'contact.html')

def blogs(request):
    try:
        data = Blog.objects.all()
        context = {"blo":data}
    except Exception as e:
        context = {"blo":"Data not found"}
    return render(request,'blog.html',context)
    
def blog1(request):
    return render(request,'b1.html')

def blog2(request):
    return render(request,'b2.html')

def blog3(request):
    return render(request,'b3.html')

def blog4(request):
    return render(request,'b4.html')

def blog5(request):
    return render(request,'b5.html')

def blog6(request):
    return render(request,'b6.html')

def profile(request):
    try:
        data = Profile.objects.all()
        context = {"pro":data}
    except Exception as e:
        context = {"pro":"Data not found"}
    return render(request,'profile.html',context)

def rec(request):
    try:
        data = Rec.objects.all()
        context = {"rec":data}
    except Exception as e:
        context = {"rec":"Data not found"}
    return render(request,'rec.html',context)


@login_required(login_url='loginPage')
def recAdd(request):
    form = RecForms()
    if request.method == 'POST':
        myData = RecForms(request.POST)
        if myData.is_valid():
            myData.save()
            messages.success(request, 'Recommendation Added Successfully')
            return redirect('rec')
    context = {"form":form}
    return render(request, 'recAdd.html', context)

@login_required(login_url='loginPage')
def recDelete(request, id):
    data = Rec.objects.get(id=id)
    data.delete()
    messages.warning(request, 'Recommendation Deleted Successfully')
    return redirect('rec')

@login_required(login_url='loginPage')
def recUpdate(request,id):
    myData = Rec.objects.get(id=id)
    updateForm = RecForms(request.POST or None, instance=myData)
    if updateForm.is_valid():
        updateForm.save()
        messages.success(request, 'Recommendation Updated Successfully')
        return redirect("rec")
    context = {"form":updateForm} 
    return render(request, 'recUpdate.html',context)