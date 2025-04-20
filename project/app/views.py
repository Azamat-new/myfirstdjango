from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def hello(request):
    return HttpResponse("Привет мир, это мое первое представление!")


def greet(request, name):
    return HttpResponse(f" Привет, {name}! Рад тебя видеть!")


def book_list(request):
    books = Book.objects.all()
    books_text = ', '.join([book.title for book in books])
    return HttpResponse(f"📚 Наши книги: {books_text}")












