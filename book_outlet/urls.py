from django.urls import path
from . import views

app_name = "book_outlet"

urlpatterns = [
    path("", views.index, name="index"),
    path("books/<int:book_id>/", views.book_detail, name="book_details"),
]
