from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Pattern Searching Algorithms")

    
def first(request):
    return HttpResponse("first")