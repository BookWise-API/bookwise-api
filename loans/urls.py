from django.urls import path
from . import views

urlpatterns = [
    path("copies/<int:pk>/", views.LoanView.as_view())
]
