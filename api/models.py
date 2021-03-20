from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

import uuid
from datetime import date


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("client-detail", args=[str(self.id)])

    def __str__(self):
        return "{0}, {1}".format(self.last_name, self.first_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True)
    summary = models.TextField(max_length=1000)

    class Meta:
        ordering = ["title", "author"]

    def display_genre(self):
        return ", ".join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = "Genre"

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey("Client", on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ("a", "Available"),
        ("l", "Loaned"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="a",
        help_text="Book availability",
    )

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return "{0} ({1})".format(self.id, self.book.title)
