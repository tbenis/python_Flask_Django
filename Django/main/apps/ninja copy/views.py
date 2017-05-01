from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, 'ninja/ninja.html')

def show(request, ninja_color):
    context ={
        "ninja_color" : ninja_color
    }
    print "*"*50
    print ninja_color
    print "*"*50
    if ninja_color == 'orange':
        return render(request, 'ninja/michealangelo.html', context)
    if ninja_color == 'blue':
        return render(request, 'ninja/leonardo.html', context)
    if ninja_color == 'red':
        return render(request, 'ninja/raphael.html', context)
    if ninja_color == 'purple':
        return render(request, 'ninja/donatello.html', context)
    else:
        return render(request, 'ninja/notapril.html', context)
