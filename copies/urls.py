from django.urls import path
from copies.views import CopieListView

urlpatterns = [
    path("copies/", CopieListView.as_view()),
]