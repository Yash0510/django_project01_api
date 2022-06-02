from django.contrib import admin
from .models import Book, User, Librarian, Publisher, Genre, Author, Language

# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Librarian)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Language)