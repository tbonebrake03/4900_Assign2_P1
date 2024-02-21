from django.contrib import admin
from .models import Movie
class MovieList(admin.ModelAdmin):
    list_display = ('name', 'director', 'year', 'description', 'rating')
    list_filter = ('name', 'director', 'year', 'rating')
    search_fields = ('name', 'description')
    ordering = ['year']

admin.site.register(Movie, MovieList)