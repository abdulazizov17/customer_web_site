
from django.shortcuts import render
from django.db.models import Min, Max, Avg, Count, Sum, OuterRef, Subquery

from app.models import Author, Book



#
# def index(request):
#     # authors = {'authors_count':3}
#     authors = Author.objects.all().aggregate(authors_count=Count('id'))
#     count = authors.get('authors_count')
#     return render(request, 'app/index.html', {'count': count})
#
# def book_list(request, books=None):
#     books = Book.objects.all().annotate(min_price=Max('price')).filter(min_price__gt = 100000000000).order_by('-min_price')
#     # print(books)
#
#
#     return render(request, 'app/index.html', {'books': books})

def magic(request):
    # authors = Author.objects.all().annotate(book_count=Count('books'))
    # books = Book.objects.values('author__name').annotate(book_count=Count('id'))
    most_expensive_book = Book.objects.filter(author_id=OuterRef('pk')).values('price').order_by('-price')[:1]
    least_expensive_book = Book.objects.filter(author_id=OuterRef('pk')).values('price').order_by('price')[:1]
    average_price = Book.objects.filter(author_id=OuterRef('pk')).values('author_id').annotate(avg_price=Avg('price')).values('avg_price')

    authors = Author.objects.annotate(
        most_popular_book = Subquery(most_expensive_book),
        least_expensive_book=Subquery(least_expensive_book),
        average_book_price=Subquery(average_price)
    )

#aggregate orqali bunisi
    # #book_stats = Book.objects.aggregate(
    #     most_expensive_book=Max('price'),
    #     least_expensive_book=Min('price'),
    #     average_book_price=Avg('price')
    # )

    # return render(request, 'app/index.html', {
    #     'book_stats': book_stats,
    # })
    return render(request,'app/index.html',{'authors':authors})