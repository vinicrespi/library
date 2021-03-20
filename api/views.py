from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin


from .models import Book, Client, BookInstance
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class BookListView(generic.ListView):

    model = Book
    paginate_by = 10


class ClientListView(generic.ListView):

    model = Client
    paginate_by = 10


class LoanedBooksByClientListView(generic.ListView):

    model = BookInstance
    paginate_by = 10

    def get_queryset(self, client_id):
        return (
            BookInstance.objects.filter(borrower=client_id)
            .filter(status__exact="l")
            .order_by("due_back")
        )

class BookReserveView(PermissionRequiredMixin, UpdateView):
    model = BookInstance
    fields = ["status"]
    permission_required = "api.can_mark_returned"


class ClientCreate(PermissionRequiredMixin, CreateView):
    model = Client
    fields = ["first_name", "last_name"]
    permission_required = "api.can_mark_returned"


class ClientUpdate(PermissionRequiredMixin, UpdateView):
    model = Client
    fields = ("__all__")
    permission_required = "api.can_mark_returned"


class ClientDelete(PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("clients")
    permission_required = "api.can_mark_returned"


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ["title", "author", "summary"]
    permission_required = "api.can_mark_returned"


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ["title", "author", "summary"]
    permission_required = "api.can_mark_returned"


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("books")
    permission_required = "api.can_mark_returned"
