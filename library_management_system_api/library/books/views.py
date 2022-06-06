from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


# Create your views here.
from .viewshelper import listbooks, removebooks, addbooks


class ListBook(generics.ListAPIView):
    queryset = listbooks()
    serializer_class = BookSerializer

class DeleteBook(generics.DestroyAPIView):
    queryset = removebooks()
    serializer_class = BookSerializer

class AddBook(generics.CreateAPIView):
    queryset = addbooks()
    serializer_class = BookSerializer