from django.urls import path
from books.views import BookListView, BookCreateView, BookDetailsView

urlpatterns = [
    path("books/", BookListView.as_view()),
    path("books/register/", BookCreateView.as_view()),
    path("books/<int:pk>/", BookDetailsView.as_view()),
]
