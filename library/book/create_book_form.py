from django import forms
from .models import Book

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'title', 'publication_year', 'date_of_issue', 'authors']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year of Publication'}),
            'date_of_issue': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

