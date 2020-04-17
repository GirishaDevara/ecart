from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {"all_items": items})


def edititem(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        image_url = request.POST.get('imgurl')
        description = request.POST.get('description')
        item.name = name
        item.cost = cost
        item.image_url = image_url
        item.description = description
        item.save()
        messages.success(request, 'Details Updated')
        return redirect(index)
    else:
        return render(request, 'edititem.html', {"item": item})


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        image_url = request.POST.get('imgurl')
        description = request.POST.get('description')
        item = Item(name=name, cost=cost, image_url=image_url, description=description)
        item.save()
        messages.info(request, "New item added")
        return redirect(index)
    else:
        return render(request, 'createitem.html')


def delete(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    messages.warning(request, 'item deleted')
    return redirect(index)


def itemdetails(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'itemdetails.html', {'item': item})


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username = first_name+last_name,email=email,password=password)
        user.save()
        return redirect(index)
    else:
        return render(request, 'registration.html')
