from django.shortcuts import render
from requests import request

# Create your views here.
def metodologia(request):
    return render(request,'metodologia/index.html')