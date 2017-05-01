from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):

    return render(request, 'beltReviewer/logReg.html')
def rProcess(request):
    postData = {
        'fname' : request.POST['fname'],
        'lname' : request.POST['lname'],
        'email' : request.POST['email'],
        'pw' : request.POST['pw'],
        'cpw' : request.POST['cpw'],
    }
    flag = User.objects.validReg(postData)
    if flag[0]:

    if not flag[0]:
        messages.success(request, flag[1].first_name)
        return redirect("/success")
def reg(request):


        return render(request, "beltReviewer/home.html")
