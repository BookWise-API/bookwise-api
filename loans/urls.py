from django.urls import path
from . import views

urlpatterns = [
    path("books/<int:pk>/", views.LoanView.as_view())
]