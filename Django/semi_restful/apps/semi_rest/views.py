from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def index(request):
    # Product.objects.all().delete()
    allp = Product.objects.all()
    context={
        'products' : allp
    }
    return render(request, 'semi_rest/index.html', context)
def show(request, id):
    id = Product.objects.filter(id = id)
    context={
        'id' : id
    }
    return render(request, 'semi_rest/productinfo.html', context)
def new(request):

        return render(request, 'semi_rest/new_product.html')
def edit(request, id):
    upd = Product.objects.filter(id = id)
    context ={
        "updates" : upd
    }
    return render(request, 'semi_rest/edit.html', context)
def create(request):
    if request.method == 'POST':
        print "&"*30
        print request.method
        print "&"*30
        Product.objects.create(name = request.POST['name'], description= request.POST['description'], price=request.POST['price'])
    return redirect('/')
def update(request, id):
    # Product.objects.get(id = id)

    print id
    obj = Product.objects.get(id=id)
    obj.name = request.POST['name']
    obj.description = request.POST['description']
    obj.price = request.POST['price']
    obj.save()

    # Product.objects.filter(id = id).update(name =request.POST['name'], description =request.POST['description'], price =request.POST['price'])
    # Product.objects.save(id = id)

    return redirect('/')
def destroy(request, id):
    Product.objects.filter(id = id).delete()
    return redirect("/")
