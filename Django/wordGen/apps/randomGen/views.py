from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):

    return render(request, 'randomGen/index.html')

def generate(request):
    print "*"* 50
    print(request.method)
    print "*"* 50
    if request.method == "POST":
        request.session['rand'] = get_random_string(length=14)
        if 'counter' in request.session:
            request.session['counter'] = request.session['counter'] + 1
        else:
            request.session['counter'] = 1
        return redirect('/gen')
    else:
        return redirect('/')
