from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "get_authors",
        "publication_year",
        "count",
    )
    list_filter = ("publication_year", "authors")
    search_fields = (
        "name",
        "description",
    )
    fieldsets = (
        (
            "Static Information",
            {
                "fields": ("title", "authors", "publication_year"),
                "description": "Information that does not change over time.",
            },
        ),
        (
            "Dynamic Information",
            {
                "fields": ("date_of_issue", "count", "description"),
                "description": "Information that changes over time.",
            },
        ),
    )

    def get_authors(self, obj):

        return ", ".join([author.name for author in obj.authors.all()])

    get_authors.short_description = "Authors"


admin.site.register(Book, BookAdmin)
