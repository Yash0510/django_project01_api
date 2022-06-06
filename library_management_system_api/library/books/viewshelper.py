from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


def listbooks():
    return Book.objects.all()

def removebooks():
    return Book.objects.all()

def addbooks():
    return Book.objects.all()
