from django import forms
from book.models import Book
from author.models import Author

class BookFilterForm(forms.Form):
    """
    A form for filtering books by various criteria.
    """
    QUERY_CHOICES = [
        ('author', 'Author Name'),
        ('user', 'User ID'),
    ]

    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search...'}),
        label="Search",
    )
    filter_by = forms.ChoiceField(
        choices=QUERY_CHOICES,
        required=False,
        label="Filter By",
        initial='name',
    )
