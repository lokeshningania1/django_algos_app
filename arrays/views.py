from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Array Data structures")

    
def first(request):
    return HttpResponse("first operation")