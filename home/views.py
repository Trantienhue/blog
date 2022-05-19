from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,  'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')
def Error(request, exception):
    return render(request, 'pages/Error.html')
def Errors(request):
    return render(request, 'pages/Error.html')