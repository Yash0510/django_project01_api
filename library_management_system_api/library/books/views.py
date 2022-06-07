from rest_framework import generics

from .models import Book, Genre, Author, Publisher, Language
from .serializers import BookSerializer, GenreSerializer, LanguageSerializer, PublisherSerializer, AuthorSerializer


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

class AddGenre(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class AddAuthor(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AddLanguage(generics.CreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class AddPublisher(generics.CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer