from django.urls import path
from . import views


urlpatterns = [
    path("copies/", views.CopieListView.as_view()),
]
