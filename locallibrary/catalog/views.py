from django.shortcuts import render
from django.views import generic
from catalog.models import Book, Author, BookInstance, Genre

# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.all().count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'catalog/index.html', context=context)
    
    
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is test book data'
        return context
        
class BookDetailView(generic.DetailView):
    model = Book
    
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = super(AuthorListView, self).get_context_data(**kwargs)
        context['some_author'] = 'This is test author data'
        return context
        
class AuthorDetailView(generic.DetailView):
    model = Author