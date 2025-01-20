from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from book.models import Book
from author.models import Author
from authentication.models import CustomUser
from book.book_filter_form import BookFilterForm
from book.create_book_form import CreateBookForm
from order.models import Order

def books_list(request):
    books = Book.objects.all()
    query = request.GET.get('query', '').strip()
    filter_by = request.GET.get('filter_by', 'name')

    if query:
        if filter_by == 'name':
            books = books.filter(name__icontains=query)
        elif filter_by == 'author':
            authors = Author.objects.filter(name__icontains=query) 
            books = books.filter(id__in=[book.id for author in authors for book in author.books.all()])  

    return render(request, 'books_list.html', {'books': books.distinct(),})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})


def books_by_user(request):
    books = []
    user = None
    form = BookFilterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        filter_by = form.cleaned_data.get('filter_by')
        query = form.cleaned_data.get('query')

        if filter_by == 'user' and query:
            user = CustomUser.get_by_id(int(query))
            if user:
                orders = Order.objects.filter(user=user)
                books = [order.book for order in orders]
        elif filter_by == 'author':
            authors = Author.objects.filter(name__icontains=query) 
            books = Book.objects.all()
            books = books.filter(id__in=[book.id for author in authors for book in author.books.all()]) 

    return render(request, 'books_by_user.html', {'books': books, 'user': user, 'form': form})

def book_create(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('books_list')
    else:
        form = CreateBookForm()
    
    return render(request, 'book_create.html', {'form': form})
