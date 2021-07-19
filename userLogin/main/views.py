from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

def home(request):
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
    user_list = User.objects.filter(email=request.POST['email'])
    print(user_list)
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

def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    if 'log_user_id' not in request.session:
        return redirect('/')

    context={
        'user': User.objects.get(id=request.session['log_user_id'])
    }
    return render(request,'dashboard.html',context)


# Create your views here.
