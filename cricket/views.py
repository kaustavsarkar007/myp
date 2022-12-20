from django.shortcuts import render
from .models import CricPost
# Create your views here.

def cricHome(request):
    post = CricPost.objects.all()
    rec =  CricPost.objects.all()[2::-1]  ## reversing the order to see latest articels
    params = {'post':post,'rec':rec}
    return render (request, 'cricket/crickethome.html',params)

def cricPost(request,slug):
    cric = CricPost.objects.filter(slug=slug).first()
    params = {'cric':cric}
    return render(request, 'cricket/cricpost.html',params)