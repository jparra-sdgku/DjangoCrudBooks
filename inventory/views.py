from django.shortcuts import redirect, render
from .forms import BookForm
from .models import Book
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView,UpdateView


# Create your views here.
def inventory_page(request):
    books_list = Book.objects.all()
    return render(request, 'inventory/inventory.html',{'books_list': books_list})

class InventoryListView(ListView):
    model = Book
    template_name = 'inventory/inventory.html'
    context_object_name = 'books_list'

def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_page')
    else:
        form = BookForm()
    return render(request,  'inventory/add_book.html', {'form': form})


class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'inventory/add_book.html'
    success_url = reverse_lazy('inventory_page')


def edit_book_view(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('inventory_page')
    else:
        form = BookForm(instance=book)
    return render(request, 'inventory/edit_book.html', {'form': form, 'book': book})

class UpdateBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'inventory/edit_book.html'
    success_url = reverse_lazy('inventory_page')


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

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'inventory/delete_book.html'
    success_url = reverse_lazy('inventory_page')








