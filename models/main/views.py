from django.shortcuts import render , HttpResponse, redirect

def index(request):
    return render(request, "index.html")

# Create your views here.
