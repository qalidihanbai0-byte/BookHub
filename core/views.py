
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.select_related("author").prefetch_related("tags")

    query = request.GET.get("q", "").strip()
    if query:
        books = books.filter(
            Q(title__icontains=query)
            | Q(author__name__icontains=query)
            | Q(description__icontains=query)
        ).distinct()

    rating = request.GET.get("rating", "").strip()
    if rating.isdigit():
        books = books.filter(rating=int(rating))

    paginator = Paginator(books, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "core/book_list.html",
        {
            "page_obj": page_obj,
            "query": query,
            "selected_rating": rating,
        },
    )


def book_detail(request, pk):
    book = get_object_or_404(
        Book.objects.select_related("author").prefetch_related("tags"),
        pk=pk,
    )
    return render(request, "core/book_detail.html", {"book": book})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("book_detail", pk=book.pk)
    else:
        form = BookForm()

    return render(
        request,
        "core/book_form.html",
        {"form": form, "title": "Добавить книгу"},
    )


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect("book_detail", pk=book.pk)
    else:
        form = BookForm(instance=book)

    return render(
        request,
        "core/book_form.html",
        {"form": form, "title": "Редактировать книгу"},
    )


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(
        request,
        "core/book_confirm_delete.html",
        {"book": book},
    )
