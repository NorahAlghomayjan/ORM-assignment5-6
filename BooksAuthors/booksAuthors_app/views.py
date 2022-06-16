from turtle import title
from django.shortcuts import render , redirect

from .models import Authors , Books

# Create your views here.

#1
def index(request): #main page

    context = {
        'books' : Books.objects.all(),
    }
    return render(request,'index.html',context)

#2
def addBook(request): #triggred by (add button) on the main page, to add new book
    if not(request.method == 'POST'):
        return redirect('/')
    title = request.POST.get('title')
    desc = request.POST.get('desc')

    Books.objects.create(title=title,desc = desc)
    return redirect('/')

#3
def book(request,id): #triggred by (view link) in the books table to return a detailed info about specific book
    book = Books.objects.get(id=id)

    # Another Way to exclude authors that are already assigned to book..
    bookAuthors = book.authors.all()
    allAuthors = Authors.objects.all()
    authors = []
    flag = True

    for authora in allAuthors:
        for author in bookAuthors:
            if author.id == authora.id:
                flag = False
                break
        if flag :
            authors.append(authora)
        flag = True

    context = {
    'book' : book,
    'authors' : authors}
    return render(request,'book.html',context)

#4
def authors(request): #authors page contains table of all authors + add new author form.
    context = {
        'authors' : Authors.objects.all(),
    }
    return render(request,'addAuthor.html',context)

#5
def addAuthor(request): #triggred by (add button) on the authors page, to add new author
    if not(request.method == 'POST'):
        return redirect('/authors')

    first = request.POST.get('first')
    last = request.POST.get('last')
    notes = request.POST.get('notes')

    Authors.objects.create(first_name=first,last_name=last,notes=notes)

    return redirect('/authors')

#6
def author(request,id): #triggred by (view link) in the authors table to return a detailed info about specific author
    author = Authors.objects.get(id=id)
    
    books = Books.objects.exclude(authors__in = [author])

    context = {
    'author' : author,
    'books' : books}
    return render(request,'author.html',context)

#7
def authorToBook (request,authorId): #to assign an author to a selected book (from list)
    if not(request.method == 'POST'):
        return redirect('/authors')
        
    bookId = request.POST.get ('book')
    book = Books.objects.get(id=int(bookId))

    author = Authors.objects.get(id=authorId)

    author.books.add(book)
    
    return redirect(f'/author/{authorId}')

#8
def bookToAuthor (request,bookId): #to assign a book to a selected author (from list).

    if not(request.method == 'POST'):
        return redirect('/')
    authorId = request.POST.get ('author')
    author = Authors.objects.get(id=int(authorId))

    book = Books.objects.get(id=bookId)

    book.authors.add(author)
        
    return redirect(f'/book/{bookId}')