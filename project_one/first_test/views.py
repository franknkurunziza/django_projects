from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("Hello World Django")

def home(request,url):
    print(url)
    return render(request, "index.html")

def redirected(request):
    return redirect("/complete_redirected")

def complete(request):
    return render(request, "redirect.html")

def catch_all(request,url):
    print(url)
    return render(request,'catch.html')

# Create your views here.

