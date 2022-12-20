from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from cricket.models import CricPost
from football.models import FootPost

# Create your views here.
def home(request):
    foots = FootPost.objects.all()[:3]
    cricks = CricPost.objects.all()[:3]
    params = {'foots':foots, 'cricks':cricks}
  
    return render (request,'home/home.html',params)


def about(request):
    return render (request,'home/about.html')

def contact(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']

        content = request.POST['content'] 
        contact = Contact(firstname=firstname,lastname=lastname,email=email,content=content, phone=phone)
        contact.save()
        messages.success(request, 'Your query is noted. We will contact you soon')
    return render(request,'home/contact.html')

def footLand(request):
    foots = FootPost.objects.all()
    print(foots)
    return render (request,'home/home.html',{'foots':foots})