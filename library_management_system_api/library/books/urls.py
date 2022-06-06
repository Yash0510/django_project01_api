from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListBook.as_view()),
    path('books/<str:title>/', views.AddBook.as_view()),
    path('books/', views.DeleteBook.as_view()),
    path('books/<str:title>/<int:pk>/', views.DeleteBook.as_view()),
]
