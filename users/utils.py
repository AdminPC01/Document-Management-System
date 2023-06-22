from .models import Employee
from django.db.models import Q


def search_employees(response):
    search_query = ""
    if response.GET.get('search_query'):
        search_query = response.GET.get('search_query')
        employees = Employee.objects.distinct().filter(
            Q(title__icontains=search_query) |
            Q(author__name__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )
    else:
        employees = Employee.objects.all()

        return employees, search_query
