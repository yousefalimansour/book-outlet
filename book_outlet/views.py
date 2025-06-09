from django.shortcuts import get_object_or_404 ,render
from .models import Book
# Create your views here.

def index(request):
    """
    Render the index page of the book outlet.
    """
    book = Book.objects.all()
    return render(request, 'book_outlet/index.html',{
        'books': book
    })
def book_detail(request, book_id):
    """
    Render the detail page for a specific book.
    """
    # book = Book.objects.get(id=book_id)
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_outlet/book_details.html', {
        'book': book
    })