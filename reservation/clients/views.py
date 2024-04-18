from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Welcome 😊 </h1>")

def header(request):
    return render(request, 'header.html')

def add (requst):
    return render(requst, 'add.html')
