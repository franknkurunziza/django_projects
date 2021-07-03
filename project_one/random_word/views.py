from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request,'random_word.html')

def random(request):
    word= get_random_string(length=14)
    return render(request, 'random_word.html',word)

# Create your views here.
