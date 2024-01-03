from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
