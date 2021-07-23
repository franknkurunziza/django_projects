from .models import User, Wish
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from datetime import datetime

def index(request):
    return render(request,'register.html')

def create(request):
    errors=User.objects.user_valid(request.POST)

    if len(errors)>0:
        for key , value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/')

    hashed_pw=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

    user1=User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hashed_pw,
    )
    request.session['log_user_id']=user1.id

    return redirect('/dashboard')


def login(request):
    if request.method== 'POST':
        user_list = User.objects.filter(email=request.POST['email'])

        if user_list:
            logged_user = user_list[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['log_user_id'] = logged_user.id
                return redirect('/dashboard')
            else:
                messages.error(request, "Invalid email or password", extra_tags='not_found')
                return redirect('/')
        messages.error(request, "Email Not Found", extra_tags='not_found')
        return redirect('/')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    if 'log_user_id' not in request.session:
        return redirect('/')

    context={
        'user': User.objects.get(id=request.session['log_user_id']),
        'wishes':Wish.objects.filter(wished_by=request.session['log_user_id']),
        'grants':Wish.objects.filter(wish_granted=True),
    }

    return render(request,'dashboard.html',context)


def wish(request):
    context={
            'user': User.objects.get(id=request.session['log_user_id']),
    }
    return render(request,'wish.html',context)

def add_wish(request):
    if 'log_user_id' not in request.session:
        return redirect('/')

    errors=Wish.objects.wish_valid(request.POST)

    if len(errors)>0:
        for key , value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/wish_form')

    wish1=Wish.objects.create(
        item=request.POST['item'],
        description=request.POST['description'],
        wished_by=User.objects.get(id=request.session['log_user_id'])
    )
    # user=User.objects.get(id=request.session['log_user_id'])
    # wish1.liked_by.add(user)

    request.session['book_id']=wish1.id
    return redirect('/dashboard')

def delete(request,id):
    wish=Wish.objects.get(id=id)
    wish.delete()
    return redirect('/dashboard')

def edit_page(request,id):
    context={
        'wish_edit': Wish.objects.get(id=id),
        'user': User.objects.get(id=request.session['log_user_id']),
    }
    return render(request,'edit.html',context)

def update(request,id):
    wish=Wish.objects.get(id=id)
    errors = Wish.objects.wish_valid(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect(f'/{wish.id}/edit')   
    wish.item=request.POST['item']
    wish.description=request.POST['description']
    wish.save()
    return redirect(f'/dashboard')

def granting(request,id):
    wish=Wish.objects.get(id=id)
    wish.wish_granted=True
    wish.updated_at=datetime.now()
    wish.save()
    return redirect('/dashboard')

def like(request,id):
    wish_likes=Wish.objects.get(id=id)
    user=User.objects.get(id=request.session['log_user_id'])
    wish_likes.users_who_liked.add(user)
    return redirect('/dashboard')