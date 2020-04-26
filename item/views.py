import pdb

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Item, Contact
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

'''
def contactpage(request):
# form example
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(mailid = request.POST.get('mailid'),yourname= request.POST.get("yourname"),
                              subject= request.POST.get('subject'),body= request.POST.get('body'))

            contact.save()

            messages.success(request, "contact details submitted successfully!!")
            return redirect(index)

        else:
            return render(request, "contact.html", {'form': form})
    else:
        # contact_obj = Contact.objects.last()
        form = ContactForm()
        return render(request, "contact.html",{'form':form})'''

"""
def contactpage(request):
    # model form example
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"details updated successfully")
            return redirect(reverse('index'))
        else:
            form = ContactForm()
            return render(request, "contact.html", {'form': form})
        # import pdb;pdb.set_trace()
    else:
        contact_obj = Contact.objects.last()
        form = ContactForm(instance= contact_obj)
        return render(request, "contact.html", {'form': form})
        """

def contactpage(request):
    if request.method == 'POST':
        contact = Contact(mailid=request.POST.get('mailid'), yourname=request.POST.get("yourname"),
                          subject=request.POST.get('subject'), body=request.POST.get('body'),
                          gender=request.POST.get('gender'),language=request.POST.get('language'),
                          country=request.POST.get('country'),)
        contact.save()
        messages.success(request,'contact details updated successfully!!!')
        return redirect(reverse('index'))
    else:
        return render(request,'normal_contact.html',{})

def contact_edit(request,id):
    details = Contact.objects.get(id=id)
    if request.method == 'POST':
        details.mailid = request.POST.get('mailid')
        details.yourname = request.POST.get("yourname")
        details.subject = request.POST.get('subject')
        details.body = request.POST.get('body')
        details.gender = request.POST.get('gender')
        details.language = request.POST.getlist('language')
        details.country = request.POST.get('country')
        # a = request.POST.getlist('language')
        # import pdb; pdb.set_trace()
        details.save()
        messages.success(request, 'contact details updated successfully!!!')
        return redirect(reverse('index'))
    else:
        return render(request, 'normal_contact_edit.html', {'contact': details})
