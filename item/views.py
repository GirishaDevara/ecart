import pdb

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Item
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ContactForm


def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {"all_items": items})


@login_required
def edititem(request, id):
    item = Item.objects.get(id=id)
    user = item.user
    if user == request.user:
        if request.method == "POST":
            name = request.POST.get('name')
            cost = request.POST.get('cost')
            image_url = request.POST.get('imgurl')
            description = request.POST.get('description')
            item.name = name
            item.cost = cost
            item.image_url = image_url
            item.description = description
            item.user = user
            item.save()
            messages.success(request, 'Details Updated')
            return redirect(index)
        else:
            return render(request, 'edititem.html', {"item": item})
    else:
        messages.warning(request, "permission denied")
        return redirect(index)


@login_required
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        image_url = request.POST.get('imgurl')
        description = request.POST.get('description')
        user = request.user
        item = Item(name=name, cost=cost, image_url=image_url, description=description, user=user)
        item.save()
        messages.info(request, "New item added")
        return redirect(index)
    else:
        return render(request, 'createitem.html')


@login_required
def delete(request, id):
    item = Item.objects.get(id=id)
    user = item.user
    if user == request.user:
        item.delete()
        messages.warning(request, 'item deleted')
        return redirect(index)
    else:
        messages.warning(request, "permission denied")
        return redirect(index)


@login_required
def itemdetails(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'itemdetails.html', {'item': item})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect(index)
    else:
        return render(request, 'registration.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Log in successful')
            return redirect(index)
        else:
            messages.error(request, 'Invalid User name or Password')
            return redirect(loginpage)
    else:
        return render(request, 'login.html')


def logout_page(request):
    logout(request)
    messages.info(request, "successfully logged out")
    return redirect(index)


def contactpage(request):
    contact = ContactForm()
    # pdb.set_trace()
    return render(request, "contact.html", {'form': contact})
