from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This works") # sends back a response and what is written inside is the item
