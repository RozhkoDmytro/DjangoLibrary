from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('user/', views.books_by_user, name='books_by_user'),
    path('create/', views.book_create, name='book_create'),
]