from django.shortcuts import redirect, render
from .forms import BookForm
from .models import Book
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.
class InventoryListView(LoginRequiredMixin,ListView):
    model = Book
    template_name = 'inventory/inventory.html'
    context_object_name = 'books_list'

class AddBookView(LoginRequiredMixin,CreateView):
    model = Book
    form_class = BookForm
    template_name = 'inventory/add_book.html'
    success_url = reverse_lazy('inventory_page')

class UpdateBookView(LoginRequiredMixin,UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'inventory/edit_book.html'
    success_url = reverse_lazy('inventory_page')

@login_required
def search_book_view(request):
    query = request.GET.get('q')
    books_list = Book.objects.filter(title__icontains=query)
    if query :
      return render(request, 'inventory/inventory.html', {
        'books_list': books_list,
        'query': query
    })
    else :
      return redirect('inventory_page')
class DeleteBookView(LoginRequiredMixin,DeleteView):
    model = Book
    template_name = 'inventory/delete_book.html'
    success_url = reverse_lazy('inventory_page')


def custom_404(request, exception):
    return render(request, '404.html', status=404)
