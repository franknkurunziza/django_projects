from main.models import Course, Description
from django.shortcuts import render, redirect


def course(request):
    context={
        'courses':Course.objects.all()
    }
    return render (request, 'index.html',context)

def create(request):
    new_description = Description.objects.create(
        desc=request.POST['desc'],
    )
    Course.objects.create(
        name=request.POST['name'],
        desc=new_description
    )
    return redirect('/courses')
# Create your views here.
