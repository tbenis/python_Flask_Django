from django.shortcuts import render, redirect
from .models import User, Friendship

# Create your views here.
def index(request):
    context ={
    'people' : User.objects.all(),
    'friendship' : Friendship.objects.all()
    }
    return render(request, 'friendOnFriends/index.html', context)

def addd(request):
    User.objects.create(name = request.POST['p1'])

    context ={
    'people' : User.objects.all,
    'friendship' : Friendship.objects.all()
}

    return render(request, 'friendOnFriends/index.html', context)
def addf(request):
    p1 = User.objects.get(id=request.POST['p1'])
    p2 = User.objects.get(id=request.POST['p2'])
    Friendship.objects.create(p1=p1,p2=p2 )
    context={
        'people' : User.objects.all,
        'friendship' : Friendship.objects.all()
     }
    return render(request, 'friendOnFriends/index.html', context)
