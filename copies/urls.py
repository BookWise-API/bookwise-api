from django.urls import path
from . import views


urlpatterns = [
    path("copies/register/", views.CopyView.as_view())
]
