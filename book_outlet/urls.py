from django.urls import path
from . import views
# namespaces مجرد تنظيم لي 
app_name = "book_outlet" 

urlpatterns = [
    path("", views.index, name="index"),
    path("books/<slug:slug>/", views.book_details, name="book_details"),
]
