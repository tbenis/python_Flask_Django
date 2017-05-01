from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
    errors = []
    User.objects.all().delete()
    return render(request, 'loginandreg/index.html')
def process(request):
    if 'lname' in request.POST and 'fname' in request.POST and 'email' in request.POST and 'passwd' in request.POST and 'confpw' in request.POST:
        check =  User.objects.validate_form(request.POST['fname'], request.POST['lname'], request.POST['email'], request.POST['passwd'], request.POST['confpw'] )   # user = User.objects.validate()
        if check == False:
            print "*"*90
            return redirect('/')
        else:
            User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], password = request.POST['passwd'])
            return render(request, 'loginandreg/success.html')
def 
