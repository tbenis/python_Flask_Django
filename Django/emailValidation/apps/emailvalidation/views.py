from django.shortcuts import render, redirect, HttpResponse
from .models import Email


# Create your views here.
def index(request):
    
    return render(request, "emailvalidation/index.html")

def process(request):
    if 'email' in request.POST:
        check = Email.objects.validate_email(request.POST['email'])
        if check == True:
            print "8"*90
            email = Email.objects.create(email = request.POST['email'])
            context={
                'email' : Email.objects.all()
            }
            return render(request, 'emailvalidation/sucess.html', context)
        else:
            context= {
                "error" : "Your Email is Invalid"
            }
            return render(request, "emailvalidation/index.html", context)

        return redirect('/')
