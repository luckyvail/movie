from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import json

# Create your views here.
def reg(request):
    return render(request,'reg.html')

def resver(request):
    return HttpResponse("ok")