from django.db import models

class genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction)")

    def __str__(self):
        return self.name

class book(models.Model):

    title = models.CharField(max_length=200)

    author = models.ForeignKey('author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")

    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.ManyToManyField(genre, help_text="Select a genre for this book")

class meta:
    ordering = ['last_name', 'first_name']


    def __str__(self):
        return self.title