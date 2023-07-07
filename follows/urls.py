from django.urls import path
from . import views

urlpatterns = [
    path("books/<int:pk>/follow/", views.FollowView.as_view())
]