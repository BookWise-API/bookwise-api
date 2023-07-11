from django.urls import path
from . import views


urlpatterns = [
    path("copies/register/", views.CopieView.as_view()),  
    path("copies/", views.CopieListView.as_view()),
]
