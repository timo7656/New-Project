# from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the diary index.")
    name = "jun"
    return render(request, "index.html", { "name" : name   })
