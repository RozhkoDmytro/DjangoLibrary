from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "display_full_name", "name", "surname", "patronymic")
    search_fields = ("name", "surname", "patronymic")
    list_filter = ("surname",)

    def display_full_name(self, obj):
        return f"{obj.name} {obj.surname} {obj.patronymic}"

    display_full_name.short_description = "Full Name"
