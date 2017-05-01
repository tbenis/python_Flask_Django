from django.shortcuts import render, redirect
from .models import Blog, Comment
# Create your views here.
def index(request):
    # Blog.objects.all().delete()
    # Comment.objects.all().delete()
    blogs= Blog.objects.all()
    context={
        'blogs': Blog.objects.all()
    }
    for blog in blogs:
        print blog.title
    return render(request, 'orm_practice/index.html', context)
def blogs(request):
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])

    return redirect('/')
def comments(request, id):
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], blog= blog)
    return redirect('/')
