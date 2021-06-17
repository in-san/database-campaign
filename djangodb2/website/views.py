from .forms import MemberForm
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Member
from django.contrib import messages


# Create your views here.
def home(request):
    all_memb=Member.objects.all
    return render(request,'home.html',{'all':all_memb})
def join(request):
    if request.method== "POST":
        form=MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
           # return HttpResponse("DATA SAVED")
            messages.success(request,('form is succesfully submitted'))    
            return render(request,'join.html',{})
        else:
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            passwd=request.POST['passwd']
            messages.success(request,('There is an error!!!'))
            return render(request,'join.html',{'fname':fname,
            'lname':lname,
            'email':email
            })



    messages.success(request,('form is succesfully submitted'))    
    return render(request,'join.html',{})