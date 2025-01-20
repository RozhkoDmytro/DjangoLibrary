from django.db import models
from author.models import Author  # Importing the Author model from author.models


class Book(models.Model):
    """
    Represents a book.
    """

    name = models.CharField(blank=True, max_length=128)
    description = models.CharField(blank=True, max_length=256)
    count = models.IntegerField(default=10)
    id = models.AutoField(primary_key=True)

    # Static Information
    title = models.CharField(max_length=255, verbose_name="Book Title")
    publication_year = models.PositiveIntegerField(verbose_name="Year of Publication")

    # Dynamic Information
    date_of_issue = models.DateField(
        null=True, blank=True, verbose_name="Date of Issue"
    )

    # Relationship with Authors
    authors = models.ManyToManyField(
        Author, related_name="books", verbose_name="Authors"
    )

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        """
        Magic method redefined to show class and ID of the Book object.
        """
        return f"Book(id={self.id})"

    @staticmethod
    def get_by_id(book_id):
        """
        Fetch a book by its ID.
        """
        return Book.objects.filter(id=book_id).first()

    @staticmethod
    def delete_by_id(book_id):
        """
        Delete a book by its ID.
        """
        book = Book.get_by_id(book_id)
        if book:
            book.delete()
            return True
        return False

    @staticmethod
    def create(name, description, count=10, authors=None):
        """
        Create a new book and associate it with authors.
        """
        if len(name) > 128:
            return None

        book = Book.objects.create(name=name, description=description, count=count)
        if authors:
            book.authors.set(authors)
        book.save()
        return book

    def to_dict(self):
        """
        Convert book information to a dictionary format.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "count": self.count,
            "authors": [author.name for author in self.authors.all()],
        }

    def update(self, name=None, description=None, count=None):
        """
        Update book attributes.
        """
        if name:
            self.name = name
        if description:
            self.description = description
        if count:
            self.count = count
        self.save()

    def add_authors(self, authors):
        """
        Add authors to the book.
        """
        if authors:
            self.authors.add(*authors)

    def remove_authors(self, authors):
        """
        Remove authors from the book.
        """
        if authors:
            self.authors.remove(*authors)

    @staticmethod
    def get_all():
        """
        Get all books as a list.
        """
        return list(Book.objects.all())
