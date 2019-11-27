from django.shortcuts import render, get_object_or_404
from .models import Movie, Person, Genre, Keyword
from .serializers import MovieSerializer, MovieDetailSerializer, PersonSerializer, PersonDetailSerializer, GenreSerializer, GenreDetailSerializer, KeywordSerializer, KeywordDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

# Create your views here.
@api_view(['GET'])
def movies(request):
    movies_all = Movie.objects.all()
    serializer = MovieSerializer(movies_all, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'POST':
        movie = MovieDetailSerializer(data=request.POST)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)

        return Response(status=400)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=204)

    else:
        return Response(status=405)


@api_view(['GET'])
def persons(request):
    persons_all = Person.objects.all()
    serializer = PersonSerializer(persons_all, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def person_detail(request, pk):
    person = Person.objects.get(pk=pk)
    serializer = PersonDetailSerializer(person)
    return Response(serializer.data)


@api_view(['GET'])
def keywords(request):
    keywords_all = Keyword.objects.all()
    serializer = KeywordSerializer(keywords_all, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    serializer = KeywordDetailSerializer(keyword)
    return Response(serializer.data)


@api_view(['GET'])
def genres(request):
    genres_all = Genre.objects.all()
    serializer = GenreSerializer(genres_all, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genre_detail(request, pk):
    genre = Genre.objects.get(pk=pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)


@api_view(['GET'])
def pick_n(request, num=1):
    user = request.user
    movie_num = Movie.objects.count()
    seen = set(user.seen_movies.all())
    unseen = set(i for i in range(1, movie_num+1))-set(seen)
    pick_num = random.sample(unseen, min(len(unseen), num))
    picked = Movie.objects.filter(pk__in=pick_num)
    serializer = MovieDetailSerializer(picked, many=True)
    return Response(serializer.data)
