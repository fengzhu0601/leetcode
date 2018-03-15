from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book


# Create your views here.


def search_form(request):
    return render_to_response('search_form.html')


def search1(request):
    if 'q' in request.GET:
        message = 'You searched for:%r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def search2(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html', {'books':books, 'query':q})
    else:
        return HttpResponse('please submit a search term.')


def search3(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books, 'query': q})
    return render_to_response('search_form.html', {'error': error})


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})



