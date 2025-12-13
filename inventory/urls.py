from django.urls import path
from . import views

urlpatterns = [
    # Rutas que usan las Vistas Basadas en Clases (CBV)
    path('inventory/', views.InventoryListView.as_view(), name='inventory_page'),
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('edit_book/<int:pk>/', views.UpdateBookView.as_view(), name='edit_book'),
    path('delete_book/<int:pk>/', views.DeleteBookView.as_view(), name='delete_book'),
    # Ruta para la búsqueda
    path('search_book/', views.search_book_view, name='search_book'),
]