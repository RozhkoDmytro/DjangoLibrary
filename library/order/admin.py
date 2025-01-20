from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "book",
        "created_at",
        "plated_end_at",
        "end_at",
        "is_returned",
    )
    list_filter = ("created_at", "plated_end_at", "end_at")
    search_fields = ("user__username", "book__title", "id")

    def is_returned(self, obj):
        """Indicates whether the book has been returned."""
        return obj.end_at is not None

    is_returned.boolean = True
    is_returned.short_description = "Returned Status"
