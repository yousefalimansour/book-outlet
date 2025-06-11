from django.shortcuts import get_object_or_404 ,render
from .models import Book
from django.db.models import Avg
# Create your views here.

def index(request):
    """
    Render the index page of the book outlet.
    """
    book = Book.objects.all()
    count_books = book.count()
    avg_rating = book.aggregate(Avg("rating"))
    return render(request, 'book_outlet/index.html',{
        'books': book,
        'count_of_books' : count_books,
        'avrage_of_rating' : avg_rating
    })
def book_details(request, slug):
    """
    Render the detail page for a specific book.
    """
    # book = Book.objects.get(id=book_id)
    book = get_object_or_404(Book, slug = slug)
    return render(request, 'book_outlet/book_details.html', {
        'book': book
    })
