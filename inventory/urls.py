from django.urls import path
from . import views

urlpatterns = [
    #path('inventory/', views.inventory_page, name='inventory_page'),
    path('inventory/', views.InventoryListView.as_view(), name='inventory_page'),
   # path('add_book/', views.add_book_view, name='add_book'),
    #path('edit_book/<int:id>/', views.edit_book_view, name='edit_book'),
    path('search_book/', views.search_book_view, name='search_book'),
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('delete_book/<int:pk>/', views.DeleteBookView.as_view(), name='delete_book'),
    path('edit_book/<int:pk>/', views.UpdateBookView.as_view(), name='edit_book'),
    path('delete_book_custom/<int:id>/', views.delete_book_view, name='delete_book_custom'),

    
    ]