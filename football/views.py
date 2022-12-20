from django.shortcuts import render
from .models import FootPost
# Create your views here.
def footHome(request):
    post = FootPost.objects.all()
   
    rec =  FootPost.objects.all()[2::-1]  ## reversing the order to see latest articels
    
 
    params = {'post':post,'rec':rec}
    return render(request,'football/foothome.html', params)


def footPost(request,slug):
    foot = FootPost.objects.filter(slug = slug).first()
    
    params = {'foot':foot}
    return render(request, 'football/footpost.html',params)


def footRec(request):
    
    pass