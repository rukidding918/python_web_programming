from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book Genre.(e.g. Science Fiction)')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_legnth=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_legnth=1000, help_text='Enter a brief description of book.')
    isbn = models.CharField('ISBN', max_legnth=13, help_text='13 charactor <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book.')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])