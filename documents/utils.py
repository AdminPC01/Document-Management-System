from django.db.models import Q
from .models import Document, Category


def search_documents(response):
    search_query = ''

    if response.GET.get('search_query'):
        search_query = response.GET.get('search_query')
        documents = Document.objects.distinct().filter(
            Q(title__icontains=search_query) |
            Q(author__name__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )
    else:
        documents = Document.objects.all()

    return documents, search_query
