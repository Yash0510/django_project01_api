from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListBook.as_view()),
    path('books/book/<str:title>/', views.AddBook.as_view()),
    path('books/author/<str:title>/', views.AddAuthor.as_view()),
    path('books/language/', views.AddLanguage.as_view()),
    path('books/publisher/', views.AddPublisher.as_view()),
    path('books/genre/', views.AddGenre.as_view()),
    path('books/<int:pk>', views.DeleteBook.as_view()),
    path('books/<str:title>/<int:pk>/', views.DeleteBook.as_view()),
]
