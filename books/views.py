from django.views import generic
from .models import Book




class BookListView(generic.ListView):
    template_name='books/book_list.html'
    context_object_name ='books'
    model =Book
class BookDetailView(generic.DetailView):
    template_name='books/book_detail.html'
    model =Book


















