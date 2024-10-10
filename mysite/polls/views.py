from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def sample(request):
    return render(request, 'sample.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
