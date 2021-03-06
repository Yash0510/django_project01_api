from django.db import models


# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.publisher_name}'


class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.author_name}'


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    isbn = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    no_of_pages = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'


class BookCatalogue(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    no_of_books = models.IntegerField()

    def __str__(self):
        return f'{self.no_of_books}'


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Librarian(models.Model):
    book_catalogue = models.ForeignKey(BookCatalogue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

