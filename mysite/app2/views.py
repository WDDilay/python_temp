from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def main(request):
    return render(request, 'main.html')

def ben10(request):
    return render(request, 'ben10.html')

def tom(request):
    return render(request, 'tomandjerry.html')