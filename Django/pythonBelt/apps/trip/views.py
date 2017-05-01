from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Trip

# Create your views here.
def index(request):
    return render(request, 'trip/index.html')

def rProcess(request):
    postData = {
        "fname": request.POST['fname'],
        "lname": request.POST['lname'],
        "email": request.POST['email'],
        "password": request.POST['password'],
        "cPassword": request.POST['cPassword'],
    }
    results = User.objects.rValidate(postData)
    # (True, [err err err])
    # (False, user obj)
    if results[0]: # There were errors
        for err in results[1]:
            # print err
            messages.error(request, err) # add messages to message object
        return redirect('/')
    else:
        request.session['logged_in_user'] = results[1].id
        messages.success(request, "Hey, thanks for registering in " + results[1].first_name +" "+ results[1].last_name)
        return redirect('/success')

def lProcess(request):
    # User.objects.all().delete()
    # Trip.objects.all().delete()
    postData = {
        'email': request.POST['email'],
        'password': request.POST['password']
    }
    results = User.objects.lValidate(postData)
    if results[0]:
        request.session['logged_in_user'] = results[1].id

        messages.success(request, "Hey, thanks for logging in " + results[1].first_name +" "+ results[1].last_name )

        return redirect('/success')
    else:
        messages.error(request, results[1])
        return redirect('/')

def success(request):
    context = {
        'user' : User.objects.get(id = request.session['logged_in_user'])

    }

    return render(request, 'trip/success.html', context)
def dash(request):
    return render(request, 'trip/success.html')
def addplan(request):
    return render(request, 'trip/addtrip.html')
def tripinfo(request):
    postData = {
        'destination' : request.POST['destination'],
        'description' : request.POST['description'],
        'from' : request.POST['from'],
        'till' : request.POST['till']
        }
    planned = Trip.objects.validateTrip(postData)
    if planned[0]:
        for error in planned[1]:
            messages.error(request, error)
            return redirect('/')
    # print context
    else:
        request.session['trip'] = planned[1].id
        return redirect('/showtrip')
        # return render(request, 'trip/success.html', context)
def showtrip(request):

    trips = Trip.objects.all()
    context ={
        'trips': trips
    }
    return render(request, 'trip/success.html', context)
def clear(request):
    request.session.clear()
    return render(request, 'trip/index.html')
