from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    print "*"* 20
    print request.method
    print "*"* 20
    date = {
    "date": datetime.now(),
    "time": datetime.time(datetime.now())
    }
    return render(request, 'timedisplay/index.html', date)
