from django.shortcuts import render, redirect
from .models import Course
import datetime

# Create your views here.
def index(request):
    context ={
        'course' : Course.objects.all()
    }
    return render(request, 'survey/index.html', context)

def process(request):
    if 'name' in request.POST and 'description' in request.POST:
        print "*"*40
        name = request.POST['name']
        print name
        description = request.POST['description']
        print description
        course = Course.objects.create(name=request.POST['name'], description= request.POST['description'])
        return redirect('/')
    else:
        name = False
        description = False
 # insert into Course (name, description, created_at, updated_at) values (name, describe, now(), now())
        return redirect('/')
def page(request, id):
    context={
    'items': Course.objects.filter(id=id),
    #  'delete' : Course.objects.filter(id=id).delete()
    }

    return render(request,'survey/destroy.html', context)

def delete(request,id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
