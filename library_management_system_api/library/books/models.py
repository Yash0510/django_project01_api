from django.db import models

# Create your models here.


class Genre(models.Model):
    name= models.CharField(max_length= 100)

class Publisher(models.Model):
    publisher_name= models.CharField(max_length= 100)

class Author(models.Model):
    author_name= models.CharField(max_length= 100)

class Language(models.Model):
    name= models.CharField(max_length=50)

class Book(models.Model):
    isbn= models.CharField(max_length=50)
    title= models.CharField(max_length=200)
    genre= models.ForeignKey(Genre, on_delete= models.CASCADE)
    publisher= models.ForeignKey(Publisher, on_delete= models.CASCADE)
    language= models.ForeignKey(Language, on_delete= models.CASCADE)
    no_of_pages = models.IntegerField (blank=True, null=True)
    author = models.ForeignKey(Author, on_delete= models.CASCADE, null = True)

    def __str__(self):
        return f'{self.title}'

