from django.shortcuts import render,redirect
from .models import Show

def shows(request):
    context={
        'shows': Show.objects.all()
    }
    return render(request,'all_show.html',context)

def add_shows(request):
    return render(request,'new_show.html')

def create(request):
    # if request.method=='POST':
    #     return redirect('/new')
    
    new_show=Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        date=request.POST['date'],
        desc=request.POST['desc'],

    )
    return redirect(f'/all/{new_show.id}')

def one_show(request,id):
    context={
        'show':Show.objects.get(id=id)
    }
    return render(request,'one_show.html',context)

def delete(request,id):
    show=Show.objects.get(id=id)
    show.delete()
    return redirect('/all')

def edit_page(request,id):
    context={
        'show_edit': Show.objects.get(id=id)
    }
    return render(request,'edit.html',context)

def update(request,id):
    show=Show.objects.get(id=id)
    show.title=request.POST['title']
    show.network=request.POST['network']
    show.date=request.POST['date']
    show.desc=request.POST['desc']
    show.save()
    return redirect(f'/all/{show.id}')
# Create your views here.
