
from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "description",
            "author",
            "tags",
            "published_date",
            "isbn",
            "rating",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название книги",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Описание книги",
            }),
            "author": forms.Select(attrs={
                "class": "form-control",
            }),
            "tags": forms.SelectMultiple(attrs={
                "class": "form-control",
            }),
            "published_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),
            "isbn": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "ISBN (необязательно)",
            }),
            "rating": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 0,
                "max": 10,
            }),
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get("isbn")

        if isbn:
            isbn = isbn.strip()

        return isbn
