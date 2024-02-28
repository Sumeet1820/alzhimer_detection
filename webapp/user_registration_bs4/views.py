from django.shortcuts import render

# Create your views here.
import  allauth


def base(request):
    return render(request, 'base.html')