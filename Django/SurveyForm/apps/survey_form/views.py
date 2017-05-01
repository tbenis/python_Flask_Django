from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    return render(request, 'survey_form/index.html')

def results(request):
    print "*"*50
    print request.method
    print "*"* 50
    if request.method == "POST":
        request.session['name'] = request.POST['fullname']
        request.session['location'] = request.POST['location']
        request.session['lang'] = request.POST['lang']
        request.session['comment'] = request.POST['comment']
        if 'counter' in request.session:
            request.session['counter'] = request.session['counter'] + 1
        else:
            request.session['counter'] = 1
        print "*"*50
        print request.method
        print "*"* 50
        return render(request, 'survey_form/results.html')
    else:
        print "*"*50
        print request.method
        print "*"*50
        return render(request, 'survey_form/results.html')
