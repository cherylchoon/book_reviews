from django import forms
from django.forms import widgets
from .models import Book, Review
from django.utils.translation import ugettext_lazy as _


class BookForm(forms.ModelForm):
    authors = forms.ChoiceField(choices=[(book.id, book.author) for book in Book.objects.all()])
    class Meta:
        model = Book
        fields = ['title', 'authors', 'author']
        labels = {
            'title': _('Book Title'),
            'authors': _('Choose from the list'),
            'author': _('Or add a new author')
        }
        widgets = {
          'authors': forms.Select(attrs={'class': 'select'}),
          }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rating']
        widgets = {
          'rating': forms.NumberInput(attrs={'min': '0', 'max': '5', 'step': '1'}),
          'review': forms.Textarea(attrs={'rows': 2, 'cols': 40})
          }
