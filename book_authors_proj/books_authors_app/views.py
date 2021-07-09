from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Book, Author

def index(request):
    context={
        "books":Book.objects.all()
    }
    return render(request,'index.html',context)

def add_book(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc']
    )
    return redirect('/')

def one_book(request,book_id):
    context={
        'book':Book.objects.get(id=book_id),
        'authors':Author.objects.all()
    }
    return render(request,"book_desc.html",context)

def author(request):
    context={
        'authors':Author.objects.all()
    }
    return render(request,'author.html',context)


def create_author(request):
    errors = Author.objects.author_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/author')
    # else
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['note'],
    )
    return redirect('/author')
    # return render(request,'author.html')
def add_author(request):
    this_book=Book.objects.get(id=request.POST['book'])
    this_author=Author.objects.get(id=request.POST['author'])

    this_book.authors.add(this_author)
    return redirect(f'book/{this_book.id}')

def one_author(request,author_id):
    context={
        'author':Author.objects.get(id=author_id),
        'books':Book.objects.all()
    }
    return render(request,"author_desc.html",context)


def add_book_author(request):
    this_author=Author.objects.get(id=request.POST['author'])
    this_book=Book.objects.get(id=request.POST['book'])

    this_author.books.add(this_book)
    return redirect(f'/author/{this_author.id}')

def delete_author(request,author_id):
    author=Author.objects.get(id=author_id)
    author.delete()
    return redirect('/author')

# Create your views here.
