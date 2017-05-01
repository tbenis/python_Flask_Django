from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.
def index(request):
    return render(request, 'usersTest/index.html')
    # print User.objects.all()
    # User.objects.create(first_name="Benis", last_name="Tambe", password="123")
    # print User.objects.all()
    # u = User.objects.get(id=1)
    # print(u.first_name)
    # u.first_name ="Mindy"
    # u.save()
    # j = User.objects.get(id = 1)
    # print j.first_name
    # print User.objects.get(first_name="Benis")
    # users = User.objects.raw("SELECT * from usersTest_user WHERE id == 1")
    # for user in users:
    #     print user.first_name
    #
    # return HttpResponse("ok")
