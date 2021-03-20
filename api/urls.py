from django.urls import path

from . import views


urlpatterns = [
    path("books/", views.BookListView.as_view(), name="books"),
    path("book/<int:pk>/reserve", views.BookReserveView.as_view(), name="book-reserve"),
    path("clients/", views.ClientListView.as_view(), name="clients"),
    path("client/<int:pk>/books", views.LoanedBooksByClientListView.as_view(), name="client-borrowed"),
]


urlpatterns += [
    path("client/create/", views.ClientCreate.as_view(), name="client-create"),
    path("client/<int:pk>/update/", views.ClientUpdate.as_view(), name="client-update"),
    path("client/<int:pk>/delete/", views.ClientDelete.as_view(), name="client-delete"),
]

urlpatterns += [
    path("book/create/", views.BookCreate.as_view(), name="book-create"),
    path("book/<int:pk>/update/", views.BookUpdate.as_view(), name="book-update"),
    path("book/<int:pk>/delete/", views.BookDelete.as_view(), name="book-delete"),
]