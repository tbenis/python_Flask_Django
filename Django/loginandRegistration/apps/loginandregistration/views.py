from django.shortcuts import render
from .models import User
import bcrypt

# Create your views here.
from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
    errors = []
    User.objects.all().delete()
    return render(request, 'loginandregistration/index.html')
def process(request):
    if 'lname' in request.POST and 'fname' in request.POST and 'email' in request.POST and 'passwd' in request.POST and 'confpw' in request.POST:
        valid =  User.objects.validate_form(request.POST['fname'], request.POST['lname'], request.POST['email'], request.POST['passwd'], request.POST['confpw'] )

        if valid[0] == False:

            context = {
                'errors' : valid[1]
            }
            return render(request, 'loginandregistration/index.html', context)
        else:
            passw = request.POST['passwd']
            hashed = bcrypt.hashpw(str(passw), bcrypt.gensalt())
            obj = User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], password = request.POST['passwd'])
            context = {
                'obj' : User.objects.all(),
                'reg' : "You are sucessfully Registered"
            }
            return render(request, 'loginandregistration/success.html', context)
def login(request):
    email = User.objects.filter(email = request.POST['email'])
    print email
    return render(request, 'loginandregistration/success.html')
