from django.views import generic
from django.urls import reverse_lazy

from .models import Book




class BookListView(generic.ListView):
    template_name='books/book_list.html'
    context_object_name ='books'
    model =Book
class BookDetailView(generic.DetailView):
    template_name='books/book_detail.html'
    model =Book
class BookCreateView(generic.CreateView):
    model =Book
    fields =['title','author','content','price']
    template_name ='books/book_create.html'
class BookUpdateView(generic.UpdateView):
    model=Book
    fields =['title','content','author','price']
    template_name ='books/book_update.html'
class BookDeleteView(generic.DeleteView):
    model =Book
    template_name='books/book_delete.html'
    success_url =reverse_lazy('book_list')



















